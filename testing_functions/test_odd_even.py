import unittest

from odd_even import even_odd

class TestOddEven(unittest.TestCase):
    def test_even(self):
        even = even_odd(2)
        self.assertEqual(even, True)

    def test_odd(self):
        odd = even_odd(5)
        self.assertEqual(odd, False)


unittest.main()

    