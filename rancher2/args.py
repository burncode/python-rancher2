import argparse
from os import environ, getenv
from argparse import ArgumentTypeError, RawTextHelpFormatter
from sys import stdout, stderr, exit, argv

from rancher2.collection import Collection

class Rancher2_V3API_Args(object):
    """
    Construct and return an arguments object.
    """
    def __init__(self):
        self.commands = ['get']
        self.args     = {
            'connection': {},
            'path': None,
            'command': None,
            'query': None
        }

    def _validate_command(self, cmd):
        """
        Make sure the command is valid.
        """
        if not cmd in self.commands:
            raise ArgumentTypeError("Invalid command '{0}', must be one of: {1}".format(cmd, ', '.join(self.commands)))
        return cmd

    def _show_epilog(self):
        """
        Construct footer text, mainly for exit codes.
        """
        return '{0}'.format('\n'.join([
            'Exit Codes:',
            '0 = HTTP 200, success. Formatted JSON on stdout',
            '1 = HTTP error, see stderr for HTTP code and response body'
        ]))

    def _parse_args(self, args):
        """
        Construct arguments to form an API connection.
        """
        parser = argparse.ArgumentParser(epilog=self._show_epilog(), formatter_class=RawTextHelpFormatter)

        # Connection parameters
        parser.add_argument("--api-url", help="Rancher v3 API endpoint, env: RANCHER2_API_URL")
        parser.add_argument("--api-token", help="Rancher v3 API token, env: RANCHER2_API_TOKEN")

        # Resource parameters
        parser.add_argument("--path", help="Path to a specific resource relative to api_url")
        parser.add_argument("--query", help="Any additional query parameters to pass: --query key1,key2=val2")

        # API command
        parser.add_argument("command",
            help="The API command to run: {0}".format(', '.join(self.commands)),
            type=self._validate_command)

        # Parse provided arguments
        args = parser.parse_args(args)

        # Get all required connection flags
        self.args['connection']['api_url']   = getenv('RANCHER2_API_URL', getattr(args, 'api_url', None))
        self.args['connection']['api_token'] = getenv('RANCHER2_API_TOKEN', getattr(args, 'api_token', None))

        # Store the API resource path / query
        self.args['path'] = getattr(args, 'path', None)
        self.args['query'] = getattr(args, 'query', None)

        # Store the command
        self.args['command'] = getattr(args, 'command')

        # All connection flags required
        if not all([v for k,v in self.args['connection'].iteritems()]):
            missing_params = [k for k,v in self.args['connection'].iteritems() if not v]
            parser.print_help()
            stderr.write('\nMissing required connection flag(s): {0}\n'.format(', '.join(missing_params)))
            exit(1)

        # Params look good
        return True

    def parse(self, args):
        """
        Public method for constructing arguments.
        """
        self._parse_args(args)

    def get_collection(self):
        """
        Return the immutable collection for arguments.
        """
        return Collection.create(self.args)

    @classmethod
    def construct(cls, args=argv[1:]):
        """
        Class method for constructing and returning an arguments object.
        """
        parser = cls()
        parser.parse(args)

        # Return a formatted arguments object
        return parser.get_collection()
