"""
This file will contain integration tests ItemModel class
"""


from models.item import ItemModel
from tests.base_test import BaseTest


class ItemModelTest(BaseTest):
    """
    This class is an integration test
    for class models/item/ItemModel
    """
    def test_create_item(self):
        """

        """
        with self.app_content:
            item = ItemModel('Body', '5000.2')

            #  it's good to check if item doesn't exist in db first
            self.assertIsNone(ItemModel.find_by_name('Body'),
                              f"Item found but shouldn't be there. Item: {item.name}")

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('Body'),
                                 f"Can't find item in db. Item: {item.name}")

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('Body'),
                              f"The item still in db. Item: {item.name}")
