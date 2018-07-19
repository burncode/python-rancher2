# -*- coding: utf-8 -*-
__version__ = '0.1.post1'

from rancher2.interface import Rancher2_V3API_Interface

def cli_client():
    """
    Invoked from the command line to interact with the libraries functionality.
    """
    client = Rancher2_V3API_Interface()
    client.run()
