# api/serializers.py
"""Serializers """
from rest_framework import serializers
from .models import User, Contact, Note, Asset, Purchase, Conversation, Message

class NoteSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Note
        fields = ('id', 'date_created', 'content', 'contact')
        read_only_fields = ('date_created', 'date_modified')


class AssetSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Asset
        fields = ('id', 'make', 'model', 'year', 'equipment_type', 'shoot_price')

class PurchaseSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    #contact = ContactSerializer
    #asset = AssetSerializer(required=False, many=False)
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Purchase
        fields = ('id', 'price', 'contact', 'asset')
 

class ContactSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    notes = NoteSerializer(required=False, many=True)
    purchases = PurchaseSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'user', 'image', \
             'date_created', 'date_modified', 'industry', 'quality', 'notes',\
            'purchases')
        read_only_fields = ('date_created', 'date_modified')
    
        
    

class ContactSubSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    notes = NoteSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'image', \
            'date_created', 'date_modified', 'industry', 'quality', 'notes',\
            'purchases')      
        read_only_fields = ('date_created', 'date_modified')

class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    contacts = ContactSubSerializer(required=False, many=True)
    

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = ('id', 'first_name', 'last_name', 'image', 'date_created', \
            'date_modified', 'contacts')
        read_only_fields = ('date_created', 'date_modified')



class MessageSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Message
        fields = ('id', 'conversation', 'message')
        read_only_fields = ('date_created',)

class ConversationSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    
    messages = MessageSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Conversation
        fields = ('id', 'user', 'contact', 'messages', 'asset')

 




