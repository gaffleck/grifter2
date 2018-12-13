"""API Views"""

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, ContactSerializer, NoteSerializer, \
    AssetSerializer, PurchaseSerializer, ConversationSerializer, MessageSerializer
from .models import User, Contact, Note, Asset, Purchase, Conversation, Message

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

class NoteCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save()

class NoteDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ Friend Details View"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class AssetCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def perform_create(self, serializer):
        serializer.save()

class AssetDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ Friend Details View"""
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class PurchaseCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def perform_create(self, serializer):
        serializer.save()

class PurchaseDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ Friend Details View"""
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class ConversationCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def perform_create(self, serializer):
        serializer.save()

class ConversationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ Friend Details View"""
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

class MessageCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save()

class MessageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ Friend Details View"""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class HandleMessagesView(APIView):
    """
    Handle pending messages
    """
    
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        unsentMessages = Message.objects.all()

        return Response("OK")