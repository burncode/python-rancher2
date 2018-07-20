import json
import requests
from sys import stderr, exit

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

    def _parse_payload(self, payload):
        """
        Parse a payload argument and return a JSON object.
        """
        try:
            return json.loads(payload)
        except:
            return self._make_params(payload)

    def _make_uri(self, path):
        """
        Generate a URI, combining the API URL and the target path.
        """
        return '{0}{1}'.format(self.url, ('' if not path else '/{0}'.format(path)))

    def _http_error(self, response):
        """
        HTTP request failed. Print to stderr and exit.
        """
        err_body = response.text
        try:
            err_body = json.dumps(json.loads(response.text), indent=2)
        except:
            pass
        stderr.write('\nHTTP {0}: Request to "{1}" failed: \n\n{2}\n\n'.format(
            response.status_code, uri, err_body))
        exit(1)

    def _make_request(self, method, uri, params={}, data={}):
        """
        Wrapper method for making at HTTP request.
        """
        response = getattr(requests, method)(uri, headers=self._make_headers(), params=params, data=data)

        # Request failed
        if not response.status_code == 200:
            self._http_error(response)

        # Return the response
        return response

    def DELETE(self, path, query):
        """
        Perform a DELETE request against an API path.
        """
        return self._make_request('delete', self._make_uri(path), params=self._make_params(query))

    def PUT(self, path, payload):
        """
        Perform a PUT request against an API path.
        """
        return self._make_request('put', self._make_uri(path), data=self._parse_payload(payload))

    def POST(self, path, payload):
        """
        Perform a POST request against an API path.
        """
        return self._make_request('post', self._make_uri(path), data=self._parse_payload(payload))

    def GET(self, path, query):
        """
        Perform a GET request against an API path.
        """
        return self._make_request('get', self._make_uri(path), params=self._make_params(query))

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
        return True
