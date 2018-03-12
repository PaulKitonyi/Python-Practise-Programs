import unittest

from city_functions import city_details

class TestCityDetails(unittest.TestCase):
    def test_city_details(self):
        testcitydetails = city_details('santiago','chile')
        self.assertEqual(testcitydetails,'Santiago, Chile')

    def test_city_details_population(self):
        testcitydetails = city_details('santiago','chile','10000')
        self.assertEqual(testcitydetails, 'Santiago, Chile - population 10000')

unittest.main()