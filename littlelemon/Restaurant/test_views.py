from django.test import TestCase
from LittleLemonAPI.models import MenuItem
from LittleLemonAPI.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add a few test instances of the Menu model
        MenuItem.objects.create(title="Pizza", price=12, inventory=50)
        MenuItem.objects.create(title="Burger", price=8, inventory=30)

    def test_getall(self):
        # Fetch all objects from the MenuItem model
        items = MenuItem.objects.all()
        
        # Serialize the retrieved objects
        serialized_data = MenuItemSerializer(items, many=True).data
        
        # Assert that the data matches the expected serialized dictionary structure
        self.assertEqual(len(serialized_data), 2)
        self.assertEqual(serialized_data[0]['title'], "Pizza")