import mock
import json
import unittest
import requests

from rancher2.connection import Rancher2_V3API_Connection

class Rancher2_V3API_Connection_MockResponse(object):
    """
    Class wrapper for mocking HTTP requests.
    """
    class MockResponse(object):
        def __init__(self, json_data, status_code):
            self.json_data   = json_data
            self.status_code = status_code
            self.text        = json.dumps(json_data)

        def json(self):
            return self.json_data

    @classmethod
    def GET(cls, *args, **kwargs):
        return cls.MockResponse({'key1': 'val1'}, 200)

class Rancher2_V3API_Connection_Test(unittest.TestCase):
    """Tests for `connection.py`."""

    connection = Rancher2_V3API_Connection('https://localhost', 'dummy_token')

    @mock.patch('requests.get', side_effect=Rancher2_V3API_Connection_MockResponse.GET)
    def test_get_root_no_query(self, mock_get):
        """Test a dummy connection to API root with no query params"""

        self.assertIsInstance(self.connection.GET(None, None).json(), dict)

    @mock.patch('requests.get', side_effect=Rancher2_V3API_Connection_MockResponse.GET)
    def test_get_root_with_query(self, mock_get):
        """Test a dummy connection to API root with query params"""

        self.assertIsInstance(self.connection.GET(None, 'key1,key2=val2').json(), dict)

    @mock.patch('requests.get', side_effect=Rancher2_V3API_Connection_MockResponse.GET)
    def test_get_path_with_query(self, mock_get):
        """Test a dummy connection to a specific API path with query params"""

        self.assertIsInstance(self.connection.GET('tokens', 'key1,key2=val2').json(), dict)

    @mock.patch('requests.get', side_effect=Rancher2_V3API_Connection_MockResponse.GET)
    def test_get_auth_test(self, mock_get):
        """Test the authentication testing function"""

        self.assertTrue(self.connection.test())

if __name__ == '__main__':
    unittest.main()
