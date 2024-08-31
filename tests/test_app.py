# TODO: Migrate to pytest (https://docs.pytest.org/en/stable)
# https://docs.python.org/3/library/unittest.html
import unittest

from app import operations


class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(operations.add(10, 10), 20)


if __name__ == "__main__":
    unittest.main()
