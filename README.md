# Rancher 2 v3 API Interface

The first release of this module allows you to query the Rancher 2 v3 API with GET requests. This is a thin layer on top of doing straight cURL requests. This started as an attempt to understand using the Rancher 2 v3 API.

### Installation
The prefix option may vary depending on the system you are running.

```
$ git clone https://github.com/djtaylor/python-rancher2
$ cd python-rancher2
$ python setup.py install --prefix /usr/local
```

### CLI Usage
```
# Using only CLI options, get the API root.
$ rancher2 get --api-url https://my.rancher.local/v3 --api-token <user>:<secret>
$
# Use environment variables for authentication, get tokens from the API server
$ export RANCHER2_API_URL='https://my.rancher.local/v3'
$ export RANCHER2_API_TOKEN='<user>:<secret>'
$ rancher2 get --path tokens
$
# Supply query arguments
$ rancher2 get --path tokens --query key1,key2=val2
```

CLI dumps indented response JSON to the terminal.
