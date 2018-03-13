import unittest
from squares import square

class TestSquares(unittest.TestCase):
    def test_square(self):
        sq = square(2)
        self.assertEqual(sq, 4)

unittest.main()