"""API Views"""

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import UserSerializer, ContactSerializer, NoteSerializer, \
    AssetSerializer, PurchaseSerializer, ConversationSerializer, MessageSerializer, \
    TwilioMessageSerializer
from .models import User, Contact, Note, Asset, Purchase, Conversation, Message, TwilioMessage
from rest_framework.decorators import api_view
from twilio.rest import Client
import os

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

class TwilioMessageCreateView(generics.ListCreateAPIView):
    """ handle Twilio Messages""" 
    queryset = TwilioMessage.objects.all()
    serializer_class = TwilioMessageSerializer
    
    def perform_create(self, serializer):
        serializer.save()

class TwilioMessageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ Friend Details View"""
    queryset = TwilioMessage.objects.all()
    serializer_class = TwilioMessageSerializer

class HandleMessagesView(APIView):
    """
    Handle pending messages
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, format=None):
        """
        Send unsent messages
        """
        unsent_messages = Message.objects.filter(message_status='UNSENT')
        
        res = "Sent Messages to "
        account_sid = os.environ.get('ACCOUNT_SID')
        message_sid = os.environ.get('MESSAGE_SID')
        auth_token = os.environ.get('AUTH_TOKEN')

        for mes in unsent_messages:
            # Your Account Sid and Auth Token from twilio.com/console
            
            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                 body=mes.message,
                                 to= mes.conversation.contact.phone_number,
                                 messaging_service_sid= message_sid
                             )
            res += " to {} sid {}".format(mes.conversation.contact.phone_number,\
               message.sid)
            
            #check the status
            mes.message_status = 'SENT'
            mes.save()

            print(message.sid)
        
        
            

        return Response(res)