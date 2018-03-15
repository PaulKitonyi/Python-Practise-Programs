import unittest
from shopping_cart import ShoppingCart, Shop

class TestShoppingCart(unittest.TestCase):
    """A Class to Test ShoppingCart Class"""

    def setUp(self):
        """Setting up the ShoppingCart Class"""
        self.my_cart    = ShoppingCart()
        self.my_cart2   = Shop()

    def test_add_item_total(self):
        """Test if the method add_item updates total accordingly"""
        my_total = self.my_cart.add_item('Cookies', 2, 400)
        self.assertEqual(my_total, 800)
        self.assertDictEqual(self.my_cart.items, {'Cookies', 2},msg="Invalid Dictionary")

    def test_add_item_entry(self):
        """Tests whether an entry is added accordingly in the items dict"""
        my_total = self.my_cart.add_item('Cookies', 2, 400)
        self.assertEqual(my_total, 800)

    def test_remove_item_total(self):
        """Tests whether an item is removed accordingly in the items dict"""
        self.my_cart.add_item('Cookies', 5, 1500)
        self.my_cart.remove_item('Cookies', 2, 300)
        self.assertEqual(self.my_cart.total,900,"Inacurate remove method")

    def test_remove_item_entry(self):
        """Tests whether the dictionary is updated accordingly"""
        self.my_cart.add_item('Cookies', 5, 1500)
        self.my_cart.remove_item('Cookies', 2, 300)
        self.assertDictEqual(self.my_cart.items, {'Cookies', 3},msg="Invalid Dictionary")

    def test_exceeds_current_quantity(self):
        """Test that all entries are removed if the quantity exceeds the current"""
        self.my_cart.add_item('Cookies', 5, 1500)
        self.my_cart.remove_item('Cookies', 2, 300)
        self.assertEqual(self.my_cart.items, {}, msg="Doesnt remove all if the quantity exceeds the current")

    def test_checkout(self):
        """Test whether it returns the correct balance"""
        self.my_cart.add_item('Cookies', 5, 1500)
        self.my_cart.checkout(self.my_cart.checkout(700), 100)

    def test_checkout_not_enough(self):
        """Tests if the payment is enough"""
        self.my_cart.add_item('Cookies', 5, 1500)
        self.assertEqual(self.my_cart.checkout(100),"Cash paid not enough")

    def test_shop_if_subclass(self):
        """Tests whether shop inherits from ShoppingCart"""
        self.assertTrue(issubclass(Shop, ShoppingCart), msg="Shop doesnt inherits from ShoppingCart")

    def test_shop_quantity(self):
        """Tests whether Shop quantity attribute is initialized to 100"""
        self.assertEqual(self.my_cart2.quantity, 100)

    def test_override_remove_item(self):
        """Tests whether calling Shop's remove_item with no arguments decrements quantity by one."""
        self.my_cart2.add_item('Cookies', 5, 1500)
        self.my_cart2.remove_item()
        self.assertDictEqual(self.my_cart2.items, {'Cookies':5}, msg="Does not remove quantity by one")
        
# unittest.main()

        
        


        

