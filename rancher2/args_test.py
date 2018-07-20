import sys
import unittest
import argparse
import contextlib
from copy import deepcopy

import rancher2.args as rancher2_args

class Rancher2_V3API_Args_Test(unittest.TestCase):
    """Tests for `args.py`."""

    example_args = [
        'get',
        '--api-url',
        'test',
        '--api-token',
        'test',
        '--path',
        'test',
        '--query',
        'test',
        '--payload',
        '{"key":"value"}']

    def test_args_parse(self):
        """Test creating an arguments object directly with `parse`"""
        args = rancher2_args.Rancher2_V3API_Args()
        self.assertTrue(args.parse(self.example_args))

    def test_args_create(self):
        """Test creating args by calling the `construct` classmethod"""
        args = rancher2_args.Rancher2_V3API_Args()
        self.assertIsInstance(args.construct(self.example_args), tuple)

    def test_args_invalid_command(self):
        """Test args with an invalid command, should fail"""
        args = rancher2_args.Rancher2_V3API_Args()

        # Make an invalid args object
        invalid_args = deepcopy(self.example_args)
        invalid_args.pop(0)
        invalid_args.insert(0, 'unsupported_cmd')

        # Supress stderr, should fail
        @contextlib.contextmanager
        def hide_stderr():
            savestderr = sys.stderr
            class Devnull(object):
                def write(self, _): pass
                def flush(self): pass
            sys.stderr = Devnull()
            try:
                yield
            finally:
                sys.stderr = savestderr

        # This should fail
        with hide_stderr():
            with self.assertRaises(SystemExit):
                args.construct(invalid_args)

if __name__ == '__main__':
    unittest.main()
