import unittest
from factorial import factorial

class FactorialTestCase(unittest.TestCase):
    """Tests for 'factorial.py'."""

    def test_0(self):
        """Expect output to be None"""
        output = factorial(0)
        self.assertEqual(output, None)

    def test_10(self):
        """Expect output to be 3,628,800"""
        output = factorial(10)
        self.assertEqual(output, 3628800)

unittest.main()
