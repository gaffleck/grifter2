# api/serializers.py
"""Serializers """
from rest_framework import serializers
from .models import Customer, Friend, GiftRecord, Gift, GiftSuggestion

class GiftSerializer(serializers.ModelSerializer):
    """Serialize the gift"""

    class Meta:
        model = Gift
        fields = ('gift_name',)

class GiftRecordSerializer(serializers.ModelSerializer):
    """Serializer for the gift record"""

    class Meta:
        """Meta class to map serialer to model"""
        model = GiftRecord
        fields = ('gift', 'price', 'date_given', 'friend')

class GiftSuggestionSerializer(serializers.ModelSerializer):
    """Serializer for a gift suggestion"""

    class Meta:
        """ Meta to map serializer to model"""
        model = GiftSuggestion
        fields = ('gift', 'friend')


class FriendSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    gift_history = GiftRecordSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Friend
        fields = ('id', 'first_name', 'last_name', 'customer', 'gift_history',
                  'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class FriendSubSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    gift_history = GiftRecordSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Friend
        fields = ('id', 'first_name', 'last_name', 'gift_history', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class CustomerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    friends = FriendSubSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'date_created', 'date_modified', 'friends')
        read_only_fields = ('date_created', 'date_modified')

