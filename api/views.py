"""API Views"""

from rest_framework import generics
from .serializers import UserSerializer, ContactSerializer, GiftRecordSerializer, GiftSerializer, GiftSuggestionSerializer, SpecialDateTypeSerializer, SpecialDateSerializer
from .models import User, Contact, GiftRecord, Gift, GiftSuggestion, SpecialDateType, SpecialDate
import logging
logger = logging.getLogger(__name__)

class UserCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        logger.debug('saving a new customer')
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        logger.debug('saving a new customer')
        serializer.save()

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ User Details View"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ContactCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        serializer.save()

class ContactDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ Friend Details View"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

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

