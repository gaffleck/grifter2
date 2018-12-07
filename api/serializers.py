# api/serializers.py
"""Serializers """
from rest_framework import serializers
from .models import Customer, Friend, GiftRecord, Gift, GiftSuggestion, SpecialDateType, SpecialDate

class GiftSerializer(serializers.ModelSerializer):
    """Serialize the gift"""

    class Meta:
        model = Gift
        fields = ('gift_name', 'image', 'gift_description', 'source')

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

class SpecialDateTypeSerializer(serializers.ModelSerializer):
    """Serialize the model type """

    class Meta:
        """map serializer to model"""
        model = SpecialDateType
        fields = ('date_type',)

class SpecialDateSerializer(serializers.ModelSerializer):
    """ Serialize the model type"""
    date_type = SpecialDateTypeSerializer(required=True, many=False)

    class Meta: 
        model = SpecialDate
        fields = ('friend', 'date', 'date_type')

class SpecialDateSubSerializer(serializers.ModelSerializer):
    """ Serialize the model type"""
    date_type = serializers.StringRelatedField(many=False) #SpecialDateTypeSerializer(required=True, many=False)

    class Meta: 
        model = SpecialDate
        fields = ('date', 'date_type')

class FriendSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    gift_history = GiftRecordSerializer(required=False, many=True)
    special_dates = SpecialDateSubSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Friend
        fields = ('id', 'first_name', 'last_name', 'customer', 'gift_history', 'image', 'special_dates', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class FriendSubSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    gift_history = GiftRecordSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Friend
        fields = ('id', 'first_name', 'last_name', 'gift_history', 'image', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class CustomerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    friends = FriendSubSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'image', 'date_created', 'date_modified', 'friends')
        read_only_fields = ('date_created', 'date_modified')

