import unittest
from palindrome import palindrome

class PalindromeTestCase(unittest.TestCase):
    """Tests for 'palindrome.py'."""

    def test_empty_string(self):
        """Should return true when given an empty string."""
        self.assertEqual(palindrome(""), True)

    def test_one_letter_string(self):
        """Should return true when given a one letter string."""
        self.assertEqual(palindrome("a"), True)

    def test_palindrome(self):
        """Should return true when given the string 'racecar'."""
        self.assertEqual(palindrome("racecar"), True)

    def test_non_palindrome(self):
        """Should return false when given a non palindromes."""
        self.assertEqual(palindrome("yolo"), False)
        self.assertEqual(palindrome("magic"), False)

unittest.main()
