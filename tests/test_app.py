# TODO: Migrate to pytest (https://docs.pytest.org/en/stable)
# https://docs.python.org/3/library/unittest.html
import subprocess
import unittest

from app import operations


class TestApp(unittest.TestCase):
    def test_add_operation(self):
        self.assertEqual(operations.add(10, 10), 20)

    def test_add_command(self):
        # https://docs.python.org/3/library/subprocess.html#subprocess.check_output
        # We set shell to True to ensure that we can "see" the python command.
        out = subprocess.check_output("python -m app add 10 10", shell=True)
        self.assertEqual(out, b"10 + 10 = 20\n")


if __name__ == "__main__":
    unittest.main()
