import unittest
import lpf

class RSTestCase(unittest.TestCase):
    """Tests for 'lpf.py'."""

    def test_get_factors(self):
        """Does n = 10 return all factors of 10?"""
        output = lpf.all_factors(10)
        self.assertEqual(output, [1, 2, 5, 10])

    def test_prime_3(self):
        """Does prime return true for prime numbers?"""
        output = lpf.prime(3)
        self.assertEqual(output, True)

    def test_prime_97(self):
        """Does prime return true for prime numbers?"""
        output = lpf.prime(97)
        self.assertEqual(output, True)

    def test_prime_0(self):
        """Does prime return false for non-prime numbers?"""
        output = lpf.prime(0)
        self.assertEqual(output, False)

    def test_prime_1(self):
        """Does prime return false for non-prime numbers?"""
        output = lpf.prime(1)
        self.assertEqual(output, False)

    def test_prime_10(self):
        """Does prime return false for non-prime numbers?"""
        output = lpf.prime(10)
        self.assertEqual(output, False)

    def test_prime_factors(self):
        """Does prime_factors return list of only prime numbers?"""
        all_factors = lpf.all_factors(10)
        primes = lpf.prime_factors(all_factors)
        self.assertEqual(primes, [2, 5])

    def test_largest_prime_factor_100(self):
        """Does largest_prime_factor return the largest prime number?"""
        output = lpf.largest_prime_factor(99)
        self.assertEqual(output, 11)

    def test_largest_prime_factor_0(self):
        """Does largest_prime_factor return the largest prime number?"""
        output = lpf.largest_prime_factor(0)
        self.assertEqual(output, None)

unittest.main()
