import datetime as date


class Item:
    """Represents The User Model"""

    def __init__(self, item_id, item_name, item_price, item_quantity, item_type):
        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_type = item_type
        self.date_created = date.datetime.now()

    def validate_data(self):
        errors = []
        if not isinstance(self.item_quantity, int):
            errors.append('Item quantity must be an integer')
        if int(self.item_quantity) < 1:
            errors.append("Item quantity must be more than 0")
        if not isinstance(self.item_price, float):
            errors.append('Item price must be a float')
        if float(self.item_price) < 1:
            errors.append("Item price must be more than 0")
        return errors

    def details(self):
        return dict(
            item_id=self.item_id,
            item_name=self.item_name,
            item_price=self.item_price,
            item_quantity=self.item_quantity,
            item_type=self.item_type,
            date_created=self.date_created
        )
