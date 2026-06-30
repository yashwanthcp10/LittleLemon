from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

# Handles GET (list all) and POST (create new item) - Steps 4 & 5
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# Handles GET (single item), PUT (update item), and DELETE (remove item) - Steps 6 & 7
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer