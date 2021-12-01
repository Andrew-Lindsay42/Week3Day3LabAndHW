import unittest

from models.shoe_order import ShoeOrder

class TestShoeOrder(unittest.TestCase):
    def setUp(self):
        self.shoe_order = ShoeOrder('Andrew', '01/12/2021', 1, 'Mizuno Waverider 25', 'A classic and versatile training shoe', 129.99)

    def test_order_has_customer_name(self):
        self.assertEqual('Andrew', self.shoe_order.customer_name)

    def test_order_has_date(self):
        self.assertEqual('01/12/2021', self.shoe_order.order_date)

    def test_order_has_quantity(self):
        self.assertEqual(1, self.shoe_order.quantity)
        
    def test_order_has_brand(self):
        self.assertEqual('Mizuno Waverider 25', self.shoe_order.shoe_brand)

    def test_order_has_description(self):
        self.assertEqual('A classic and versatile training shoe', self.shoe_order.shoe_description)

    def test_order_has_price(self):
        self.assertEqual(129.99, self.shoe_order.shoe_price)