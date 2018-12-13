"""API Views"""

from rest_framework import generics
from .serializers import UserSerializer, ContactSerializer
from .models import User, Contact
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
