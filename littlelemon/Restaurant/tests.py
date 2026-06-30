from django.test import TestCase
from LittleLemonAPI.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create an instance with the values specified in the video instructions
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        
        # Verify that get_item() returns the anticipated string format
        self.assertEqual(item.get_item(), "IceCream : 80")