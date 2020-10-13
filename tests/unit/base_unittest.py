"""
This file will contain a class which will set up
an attributes for the unit1 test
"""

from unittest import TestCase
from models.item import ItemModel


class BaseUnitTest(TestCase):
    """
    This class will setup a testing class
    """
    def setUp(self):
        """
        This class is called before every test.
        """
        self.item1 = ItemModel('Head', '1000')
        self.item2 = ItemModel('Leg', '500')
