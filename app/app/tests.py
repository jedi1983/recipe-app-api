

from django.test import TestCase
from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """ Test Case to add two number together """
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """ Test Case for substract two numbers """
        self.assertEqual(subtract(5, 11), 6)
