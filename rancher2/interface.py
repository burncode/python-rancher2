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

    def get(self):
        """
        Get a remote resource.
        """
        response = self.connection.GET(self.args.path, self.args.query)
        stdout.write('{0}\n'.format(json.dumps(json.loads(response.text), indent=2)))
        exit(0)

    def run(self):
        """
        Run the client with the given arguments.
        """
        self.connection.test()

        # Run the command
        getattr(self, self.args.command)()
