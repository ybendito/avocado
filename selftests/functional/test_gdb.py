import os
import tempfile
import unittest

from avocado.utils import process

from .. import AVOCADO, BASEDIR, temp_dir_prefix


class GDBPluginTest(unittest.TestCase):

    def setUp(self):
        prefix = temp_dir_prefix(__name__, self, 'setUp')
        self.tmpdir = tempfile.TemporaryDirectory(prefix=prefix)

    def test_gdb_prerun_commands(self):
        os.chdir(BASEDIR)
        cmd_line = ('%s run --job-results-dir %s --sysinfo=off '
                    '--gdb-prerun-commands=/dev/null passtest.py'
                    % (AVOCADO, self.tmpdir.name))
        process.run(cmd_line)

    def test_gdb_multiple_prerun_commands(self):
        os.chdir(BASEDIR)
        cmd_line = ('%s run --job-results-dir %s --sysinfo=off '
                    '--gdb-prerun-commands=/dev/null '
                    '--gdb-prerun-commands=foo:/dev/null passtest.py'
                    % (AVOCADO, self.tmpdir.name))
        process.run(cmd_line)

    def tearDown(self):
        self.tmpdir.cleanup()


if __name__ == '__main__':
    unittest.main()
