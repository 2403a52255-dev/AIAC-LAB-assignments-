import unittest

class ShoppingCart:
    def _init_(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total_cost(self):
        return sum(self.items.values())


class TestShoppingCart(unittest.TestCase):

    def test_add_and_total(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.0)
        cart.add_item("banana", 0.5)
        self.assertEqual(cart.total_cost(), 1.5)

    def test_remove_item(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.0)
        cart.add_item("banana", 0.5)
        cart.remove_item("apple")
        self.assertEqual(cart.total_cost(), 0.5)

    def test_update_item_price(self):
        cart = ShoppingCart()
        cart.add_item("chocolate", 2.0)
        cart.add_item("chocolate", 3.0)  # Overwrites old price
        self.assertEqual(cart.total_cost(), 3.0)

    def test_remove_non_existent_item(self):
        cart = ShoppingCart()
        cart.add_item("juice", 1.5)
        cart.remove_item("candy")  # Not present
        self.assertEqual(cart.total_cost(), 1.5)

    def test_empty_cart_total(self):
        cart = ShoppingCart()
        self.assertEqual(cart.total_cost(), 0)

    def test_zero_price_item(self):
        cart = ShoppingCart()
        cart.add_item("free_sample", 0.0)
        self.assertEqual(cart.total_cost(), 0.0)

    def test_negative_price_item(self):
        cart = ShoppingCart()
        cart.add_item("discount_coupon", -5.0)
        self.assertEqual(cart.total_cost(), -5.0)

    def test_multiple_add_and_remove(self):
        cart = ShoppingCart()
        cart.add_item("pen", 1.0)
        cart.add_item("pencil", 0.5)
        cart.add_item("notebook", 2.5)
        self.assertEqual(cart.total_cost(), 4.0)
        cart.remove_item("pencil")
        self.assertEqual(cart.total_cost(), 3.5)
        cart.remove_item("pen")
        self.assertEqual(cart.total_cost(), 2.5)


if __name__ == "_main_":
    unittest.main()