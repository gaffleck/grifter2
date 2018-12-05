# api/serializers.py
"""Serializers """
from rest_framework import serializers
from .models import Customer, Friend

class FriendSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Friend
        fields = ('id', 'first_name', 'last_name', 'customer', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class FriendSubSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Friend
        fields = ('id', 'first_name', 'last_name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class CustomerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    friends = FriendSubSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'date_created', 'date_modified', 'friends')
        read_only_fields = ('date_created', 'date_modified')
