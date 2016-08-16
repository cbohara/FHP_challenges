import unittest
from lcs import lcs

class TestLCS(unittest.TestCase):
    """Test longest common subsequence challenge functions."""

    def test_none_input(self):
        """Should result in None when given None."""
        self.assertEqual(lcs(None,None), None)

    def test_no_common(self):
        """Should result in None when given no common subsequences."""
        self.assertEqual(lcs("a","b"), None)

    def test_lcs(self):
        """Should return the longest subsequence when given a short string."""
        self.assertEqual(lcs("ABCDAF","ACBCF"), "ABCF")

unittest.main()
