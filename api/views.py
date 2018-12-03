# api/views.py

from rest_framework import generics
from .serializers import CustomerSerializer, FriendSerializer
from .models import Customer, Friend
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Pastebin API')


class CustomerCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        serializer.save()

class CustomerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class FriendCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def perform_create(self, serializer):
        serializer.save()

class FriendDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

