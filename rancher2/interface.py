import json
from sys import stdout,stderr,exit

from rancher2.args import Rancher2_V3API_Args
from rancher2.connection import Rancher2_V3API_Connection

class Rancher2_V3API_Interface(object):
    """
    Class for handling interactions with the CLI client.
    """
    def __init__(self, args=None):
        self.args = Rancher2_V3API_Args.construct(args)
        self.connection = Rancher2_V3API_Connection(
            self.args.connection.api_url,
            self.args.connection.api_token)

    def get(self, silent=False):
        """
        Get a remote resource.
        """
        return self.connection.GET(self.args.path, self.args.query)

    def delete(self, silent=False):
        """
        Delete a remote resource.
        """
        return self.connection.DELETE(self.args.path, self.args.query)

    def post(self):
        """
        Create a new remote resource.
        """
        return self.connection.POST(self.args.path, self.args.payload)

    def put(self):
        """
        Update an existing remote resource.
        """
        return self.connection.PUT(self.args.path, self.args.payload)

    def run(self, silent=False):
        """
        Run the client with the given arguments.
        """
        self.connection.test()

        # Run the command
        response = getattr(self, self.args.command)()

        # If showing output
        if not silent:
            stdout.write('{0}\n'.format(json.dumps(json.loads(response.text), indent=2)))
        exit(0)
