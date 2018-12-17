"""API Views"""

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import UserSerializer, ContactSerializer, NoteSerializer, \
    AssetSerializer, PurchaseSerializer, ConversationSerializer, MessageSerializer, \
    TwilioMessageSerializer, ImageSerializer
from .models import User, Contact, Note, Asset, Purchase, Conversation, Message, TwilioMessage,\
    Image
from rest_framework.decorators import api_view
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
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

class ImageCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        serializer.save()

class ImageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ Friend Details View"""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class TwilioReplyCreateView(generics.ListCreateAPIView):
    """ handle Twilio Messages""" 
    queryset = TwilioMessage.objects.all()
    serializer_class = TwilioMessageSerializer
    
    def perform_create(self, serializer):
        contact = Contact.objects.all().filter(phone_number=serializer.validated_data.get('To')).first()
        
        #twmsg = TwilioMessage(data=serializer.validated_data)
        if(contact is not None):
            #twmsg.contact_id = contact.id
            serializer.validated_data['contact_id'] = contact.id
        serializer.save()

    def post(self, request, *args, **kwargs):
        result = self.create(request, *args, **kwargs)
        resp = MessagingResponse()
        return Response("OK")

class TwilioReplyDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ Friend Details View"""
    queryset = TwilioMessage.objects.all()
    serializer_class = TwilioMessageSerializer

class TwilioMessageCreateView(generics.ListCreateAPIView):
    """ handle Twilio Messages""" 
    queryset = TwilioMessage.objects.all()
    serializer_class = TwilioMessageSerializer
    
    def perform_create(self, serializer):
        account_sid = os.environ.get('ACCOUNT_SID')
        message_sid = os.environ.get('MESSAGE_SID')
        auth_token = os.environ.get('AUTH_TOKEN')
        contact = Contact.objects.all().filter(phone_number=serializer.validated_data.get('To')).first()
        
        #twmsg = TwilioMessage(data=serializer.validated_data)
        if(contact is not None):
            #twmsg.contact_id = contact.id
            serializer.validated_data['contact_id'] = contact.id


        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=serializer.validated_data.get('Body'),
                to=serializer.validated_data.get('To'),
                messaging_service_sid=message_sid)
        serializer.save()
        #twmsg.save()

class TwilioMessageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ Friend Details View"""
    queryset = TwilioMessage.objects.all()
    serializer_class = TwilioMessageSerializer


