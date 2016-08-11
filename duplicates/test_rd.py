import unittest
from remove_duplicates import remove_duplicates

class RDTestCase(unittest.TestCase):
    """Tests for 'remove_duplicates.py'."""

    def test_output(self):
        """Are all duplicates removed?"""
        duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        output = remove_duplicates(duplicates)
        self.assertEqual(output, [1,2,3,4])

unittest.main()
