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
        response = Rancher2_V3API_Interface(self.dummy_args).get()
        self.assertEqual(response.status_code, 200)

    @mock.patch('requests.put', side_effect=Rancher2_V3API_Connection_MockResponse.PUT)
    def test_interface_put(self, mock_put):
        """Call the interface `put` method directly"""
        response = Rancher2_V3API_Interface(self.dummy_args).put()
        self.assertEqual(response.status_code, 200)

    @mock.patch('requests.post', side_effect=Rancher2_V3API_Connection_MockResponse.POST)
    def test_interface_get(self, mock_post):
        """Call the interface `post` method directly"""
        response = Rancher2_V3API_Interface(self.dummy_args).post()
        self.assertEqual(response.status_code, 200)

    @mock.patch('requests.delete', side_effect=Rancher2_V3API_Connection_MockResponse.DELETE)
    def test_interface_get(self, mock_delete):
        """Call the interface `delete` method directly"""
        response = Rancher2_V3API_Interface(self.dummy_args).delete()
        self.assertEqual(response.status_code, 200)
