import json
import requests
from sys import stderr, exit
from requests.auth import HTTPBasicAuth

class Rancher2_V3API_Connection(object):
    """
    Construct and return a v3 API connection object.
    """
    def __init__(self, url, token):
        self.url   = url
        self.token = token

    def _make_headers(self):
        """
        Construct and return a headers object.
        """
        return {
            "Authorization": "Bearer {0}".format(self.token)
        }

    def _make_params(self, params):
        """
        Construct any optional query parameters for the URL
        """
        _params = {}
        if params:
            for param in params.split(','):
                _params[param if not '=' in param else param.split('=')[0]] = True if not '=' in param else param.split('=')[1]
        return _params

    def GET(self, path, query):
        """
        Perform a GET request against an API path.
        """
        uri = '{0}{1}'.format(self.url, ('' if not path else '/{0}'.format(path)))
        response = requests.get(uri, headers=self._make_headers(), params=self._make_params(query))

        # Request failed
        if not response.status_code == 200:
            err_body = response.text
            try:
                err_body = json.dumps(json.loads(response.text), indent=2)
            except:
                pass
            stderr.write('\nHTTP {0}: Request to "{1}" failed: \n\n{2}\n\n'.format(
                response.status_code, uri, err_body))
            exit(1)

        # Return the response
        return response

    def _test_auth(self):
        """
        Test authentication against the v3 API root.
        """
        self.GET(None, None)

    def test(self):
        """
        Test the connection.
        """
        self._test_auth()
