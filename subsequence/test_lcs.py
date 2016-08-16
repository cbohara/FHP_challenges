import unittest
from lcs import create_matrix, longest_common_subsequence

class LCSTestCase(unittest.TestCase):
    """Test longest common subsequence challenge functions."""

    def test_none_input(self):
        """Should result in None when given None."""
        self.assertEqual(longest_common_subsequence(None,None), None)

    def test_no_common(self):
        """Should result in None when given no common subsequences."""
        self.assertEqual(longest_common_subsequence("a","b"), None)

    def test_lcs(self):
        """Should return the longest subsequence when given a short string."""
        self.assertEqual(longest_common_subsequence("ABCDAF","ACBCF"), "ABCF")

unittest.main()
