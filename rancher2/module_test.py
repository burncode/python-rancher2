import unittest
from subprocess import Popen, PIPE

class Collection_Test(unittest.TestCase):
    """General module level testing"""

    def test_cli_help_call(self):
        """Test CLI help call"""
        test_proc = Popen(['/usr/bin/env', 'rancher2', '--help'], stdout=PIPE, stderr=PIPE)
        try:
            test_proc.communicate()
            self.assertEquals(test_proc.returncode, 0)
        except Exception as e:
            self.fail(str(e))

    def test_cli_invalid_cmd(self):
        """Test an invalid command call, expects 2"""
        test_proc = Popen(['/usr/bin/env', 'rancher2', 'invalid'], stdout=PIPE, stderr=PIPE)
        try:
            test_proc.communicate()
            self.assertEquals(test_proc.returncode, 2)
        except Exception as e:
            self.fail(str(e))

if __name__ == '__main__':
    unittest.main()
