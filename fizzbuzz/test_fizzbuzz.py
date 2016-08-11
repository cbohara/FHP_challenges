import unittest
from fizzbuzz import fizzbuzz

class FizzbuzzTestCase(unittest.TestCase):
    """Tests for 'fizzbuzz.py'."""

    def test_fizz(self):
        """Are multiples of 3 replaced by fizz?"""
        output = fizzbuzz(4)
        self.assertEqual(output[2], 'Fizz')

    def test_buzz(self):
        """Are multiples of 5 replaced by buzz?"""
        output = fizzbuzz(10)
        self.assertEqual(output[4], 'Buzz')

    def test_fizzbuzz(self):
        """Are multiples of 3 and 5 replaced by fizzbuzz?"""
        output = fizzbuzz(20)
        self.assertEqual(output[14], 'FizzBuzz')

    def test_numbers(self):
        """Are other values printing?"""
        output = fizzbuzz(5)
        self.assertEqual(output[1], 2)

unittest.main()
