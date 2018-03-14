import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """A class to Test the Employee Class"""

    def setUp(self):
        """Create Employee for test in methods"""
        self.emp_1 = Employee('Paul', 'Kitonyi', 500)


    def test_give_default_raise(self):
        """Testing whether default raise is set automatically"""
        default = self.emp_1.give_raise()
        self.assertEqual(default, 5500)

    def test_give_custom_raise(self):
        """Testing whether Custom raise is set automatically"""
        custom = self.emp_1.give_raise(5000)
        self.assertEqual(custom, 10500)
        

unittest.main()

        
