import unittest

from src.main import greet


class TestMain(unittest.TestCase):
    def test_greet_default(self):
        self.assertEqual(greet(), "Hello, world!")

    def test_greet_custom(self):
        self.assertEqual(greet("GH-300learning"), "Hello, GH-300learning!")


if __name__ == "__main__":
    unittest.main()
