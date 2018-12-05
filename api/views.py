"""API Views"""

from rest_framework import generics
from .serializers import CustomerSerializer, FriendSerializer, GiftRecordSerializer, GiftSerializer
from .models import Customer, Friend, GiftRecord, Gift

class CustomerCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        serializer.save()

class CustomerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ Customer Details View"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class FriendCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def perform_create(self, serializer):
        serializer.save()

class FriendDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ Friend Details View"""
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class GiftRecordCreateView(generics.ListCreateAPIView):
    """view for rest API"""
    queryset = GiftRecord.objects.all()
    serializer_class = GiftRecordSerializer

class GiftRecordDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """CUD actions"""
    queryset = GiftRecord.objects.all()
    serializer_class = GiftRecordSerializer

class GiftCreateView(generics.ListCreateAPIView):
    """view for rest API"""
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer

class GiftDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """CUD actions"""
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer
