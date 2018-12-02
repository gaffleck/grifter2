# api/views.py

from rest_framework import generics
from .serializers import CustomerSerializer
from .models import Customer


class CustomerCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        serializer.save()

class CustomerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer