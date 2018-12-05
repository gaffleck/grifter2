# api/serializers.py
"""Serializers """
from rest_framework import serializers
from .models import Customer, Friend, Gift

class GiftSerializer(serializers.ModelSerializer):
    """Serializer for the gift"""

    class Meta: 
        """Meta class to map serialer to model"""
        model = Gift
        fields = ('gift_name', 'price', 'date_given', 'friend')


class FriendSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    gifts = GiftSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Friend
        fields = ('id', 'first_name', 'last_name', 'customer', 'gifts', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
    
    

class FriendSubSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    gifts = GiftSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Friend
        fields = ('id', 'first_name', 'last_name', 'gifts', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class CustomerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    friends = FriendSubSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'date_created', 'date_modified', 'friends')
        read_only_fields = ('date_created', 'date_modified')

class GiftSerializer(serializers.ModelSerializer):
    """serializer for gift"""

    class Meta: 
        """Mapping fields """
        model = Gift
        fields = ('id', 'gift_name', 'price', 'date_given', 'friend')
        
