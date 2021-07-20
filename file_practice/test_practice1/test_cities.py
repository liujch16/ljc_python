import unittest
from city_functions import country_city

class NameTestCase(unittest.TestCase):
   
    def test_city_country(self):
        formattedname = country_city('santiago', 'chile')
        self.assertEqual(formattedname, 'santiago chile')

    def test_city_country_population(self):
        formattedname = country_city('santiago', 'chile', 5000000)
        self.assertEqual(formattedname, 'santiago chile -population 5000000')

unittest.main()