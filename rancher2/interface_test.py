import mock
import unittest

from rancher2.interface import Rancher2_V3API_Interface
from rancher2.connection_test import Rancher2_V3API_Connection_MockResponse

class Rancher2_V3API_Interface_Test(unittest.TestCase):
    """Tests for `interface.py`."""

    dummy_args = [
        'get',
        '--api-url',
        'test',
        '--api-token',
        'test',
        '--path',
        'test',
        '--query',
        'key1,key2=val2']

    def test_interface_init(self):
        """Make sure we can initialize the interface"""
        self.assertIsInstance(Rancher2_V3API_Interface(self.dummy_args), Rancher2_V3API_Interface)

    @mock.patch('requests.get', side_effect=Rancher2_V3API_Connection_MockResponse.GET)
    def test_interface_get(self, mock_get):
        """Call the interface `get` method directly"""
        with self.assertRaises(SystemExit) as cm:
            Rancher2_V3API_Interface(self.dummy_args).get(silent=True)
        self.assertEqual(cm.exception.code, 0)
