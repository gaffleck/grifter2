"""API Views"""

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import UserSerializer, ContactSerializer, NoteSerializer, \
    AssetSerializer, PurchaseSerializer, ConversationSerializer, MessageSerializer
from .models import User, Contact, Note, Asset, Purchase, Conversation, Message
from rest_framework.decorators import api_view
from twilio.rest import Client

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

class MessageStatusView(CreateAPIView):
    """ get status messages from Twilio """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        #serializer = self.get_serializer(data=request.data)
        #serializer.is_valid(raise_exception=True)
        #self.perform_create(serializer)
        #headers = self.get_success_headers(serializer.data)
        #return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)       
        return Response('OK')

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

        for mes in unsent_messages:
            # Your Account Sid and Auth Token from twilio.com/console
            account_sid = 'AC02c4085896504639e775449de83fe365'
            message_sid = 'MGd627e2f9bc305bce2a2d525cc0831b07'
            auth_token = 'df7b034f87af4d5374e4928c5794aa22'
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
            mes.status = ''

            print(message.sid)
            

        return Response(res)