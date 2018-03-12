import unittest
from upper import uppercase


class TestUpper(unittest.TestCase):
    def test_uppercase(self):
        caps = uppercase('paul')
        self.assertEqual(caps, 'PAUL')


unittest.main()