from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Secured Menu views
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]  # Added per Step 2/3
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Secured Booking view
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # Added per Step 3
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer