import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py' """

    def test_first_last_name(self):
        """Do name like Paul Kitonyi Work??"""
        formatted_name = get_formatted_name('paul','Kitonyi')
        self.assertEqual(formatted_name, 'Paul Kitonyi')

unittest.main()

