import unittest
from caesar import rot13

class RDTestCase(unittest.TestCase):
    """Test for 'caesar.py'."""

    def test_empty_string(self):
        """Should be return an empty string when given an empty string."""
        self.assertEqual(rot13(""), "")

    def test_one_letter_string(self):
        """Should be ciphered when given a one letter string."""
        self.assertEqual(rot13("a"), "n")

    def test_capitalization(self):
        """Should keep the capitalization when given a set of capital and lowercase letters."""
        self.assertEqual(rot13("aB"), "nO")

    def test_capitalization_string(self):
        """Should cipher and maintain capitalization when given a string."""
        self.assertEqual(rot13("Julius ATTACK Gaul Now"), "Whyvhf NGGNPX Tnhy Abj")

    def test_full_rotation(self):
        """Should result in the same string when given two transformations."""
        input_string = "Julius ATTACK Gaul Now"
        self.assertEqual(rot13(rot13(input_string)), input_string)

unittest.main()
