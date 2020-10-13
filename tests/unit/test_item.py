"""
This file contain unit1 tests for ItemModels
"""

from tests.unit.base_unittest import BaseUnitTest


class TestItemModel(BaseUnitTest):
    """
    This class will contain unit1 tests for
    class ItemModel
    """
    def test_init(self):
        """
        This is unit1 test for creating a new object
        """
        self.assertEqual(self.item1.name, 'Head')
        self.assertEqual(self.item1.price, '1000')

        self.assertEqual(self.item2.name, 'Leg')
        self.assertEqual(self.item2.price, '500')

    def test_json(self):
        """
        This method will check if the return string from json file is
        correct
        """

        expected = {
            'name': 'Head',
            'price': '1000',
        }

        self.assertEqual(self.item1.json(), expected, "\n\nThe JSON format of the item is not correct."
                                                      "\nReceived: {}"
                                                      "\nExpected: {}".format(self.item1.json(),
                                                                              expected))

