# file name: test_name_function.py
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):  # Testes para 'name_function.py'.
    def test_first_last_name(self):  # Nomes como 'Janis Joplin' funcionam?
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang','amadeus', 'mozart')
        self.assertEqual(formatted_name, 'wolfgang Mozart Amadeus')


unittest.main()