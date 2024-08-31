import unittest

from app import operations


class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(operations.add(10, 10), 20)


if __name__ == "__main__":
    unittest.main()
