import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py' """

    def test_first_last_name(self):
        """Do name like Paul Kitonyi Work??"""
        formatted_name = get_formatted_name('paul','Kitonyi')
        self.assertEqual(formatted_name, 'Paul Kitonyi')

    def test_first_last_middle_name(self):
        """Do names like paul kitonyi musyima work???"""
        formatted_name = get_formatted_name('paul', 'kitonyi', 'musyima')
        self.assertEqual(formatted_name,'Paul Musyima Kitonyi')

unittest.main()

