# api/serializers.py
"""Serializers """
from rest_framework import serializers
from .models import User, Contact

class ContactSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'user', 'image', \
             'date_created', 'date_modified', 'industry', 'quality', 'notes',\
            'purchases')
        read_only_fields = ('date_created', 'date_modified')

class ContactSubSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    
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
        fields = ('id', 'first_name', 'last_name', 'image', 'date_created', 'date_modified', 'contacts')
        read_only_fields = ('date_created', 'date_modified')
