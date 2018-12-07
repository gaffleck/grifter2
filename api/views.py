"""API Views"""

from rest_framework import generics
from .serializers import CustomerSerializer, FriendSerializer, GiftRecordSerializer, GiftSerializer, GiftSuggestionSerializer, SpecialDateTypeSerializer, SpecialDateSerializer
from .models import Customer, Friend, GiftRecord, Gift, GiftSuggestion, SpecialDateType, SpecialDate
import logging
logger = logging.getLogger(__name__)

class CustomerCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        logger.debug('saving a new customer')
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        logger.debug('saving a new customer')
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


class GiftSuggestionDetailsView(generics.ListCreateAPIView):
    """CUD Actions"""
    queryset = GiftSuggestion.objects.all()
    serializer_class = GiftSuggestionSerializer

class GiftSuggestionCreateView(generics.ListCreateAPIView):
    """CUD Actions"""
    queryset = GiftSuggestion.objects.all()
    serializer_class = GiftSuggestionSerializer

class SpecialDateTypeDetailsView(generics.ListCreateAPIView):
    """CUD Actions"""
    queryset = SpecialDateType.objects.all()
    serializer_class = SpecialDateTypeSerializer

class SpecialDateTypeCreateView(generics.ListCreateAPIView):
    """CUD Actions"""
    queryset = SpecialDateType.objects.all()
    serializer_class = SpecialDateTypeSerializer

class SpecialDateDetailsView(generics.ListCreateAPIView):
    """CUD Actions"""
    queryset = SpecialDate.objects.all()
    serializer_class = SpecialDateSerializer

class SpecialDateCreateView(generics.ListCreateAPIView):
    """CUD Actions"""
    queryset = SpecialDate.objects.all()
    serializer_class = SpecialDateSerializer

