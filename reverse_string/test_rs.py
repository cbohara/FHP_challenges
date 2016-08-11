import unittest
from reverse_string import reverse_string

class RSTestCase(unittest.TestCase):
    """Test reverse_string.py."""

    def test_reverse(self):
        """Does an input of 'hello' return 'olleh'?"""
        output = reverse_string('hello')
        self.assertEqual(output, 'olleh')

unittest.main()
