from app.api.v1.models.items.item import Item
from app.api.v1.models.items.item_type import ItemType


class Sale(Item):
    """Represents the Store Attendant"""

    def __init__(self, s_id, s_name, s_price, s_quantity, sold_by):
        super(Sale, self).__init__(s_id, s_name, s_price, s_quantity, 'SALE')
        self.sold_by = sold_by
