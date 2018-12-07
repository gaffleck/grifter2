# api/serializers.py
"""Serializers """
from rest_framework import serializers
from .models import User, Contact, GiftRecord, Gift, GiftSuggestion, SpecialDateType, SpecialDate

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
        fields = ('gift', 'price', 'date_given', 'contact')

class GiftSuggestionSerializer(serializers.ModelSerializer):
    """Serializer for a gift suggestion"""

    class Meta:
        """ Meta to map serializer to model"""
        model = GiftSuggestion
        fields = ('gift', 'contact')

class SpecialDateTypeSerializer(serializers.ModelSerializer):
    """Serialize the model type """

    class Meta:
        """map serializer to model"""
        model = SpecialDateType
        fields = ('date_type',)

class SpecialDateSerializer(serializers.ModelSerializer):
    """ Serialize the model type"""
    #date_type = SpecialDateTypeSerializer(required=True, many=False)

    class Meta: 
        model = SpecialDate
        fields = ('contact', 'date', 'date_type')

class SpecialDateSubSerializer(serializers.ModelSerializer):
    """ Serialize the model type"""
    date_type = serializers.StringRelatedField(many=False) #SpecialDateTypeSerializer(required=True, many=False)

    class Meta: 
        model = SpecialDate
        fields = ('date', 'date_type')

class ContactSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    gift_history = GiftRecordSerializer(required=False, many=True)
    special_dates = SpecialDateSubSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'user', 'gift_history', 'image', 'special_dates', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class ContactSubSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    gift_history = GiftRecordSerializer(required=False, many=True)
    special_dates = SpecialDateSubSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'gift_history', 'image', 'date_created', 'special_dates', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    contacts = ContactSubSerializer(required=False, many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = ('id', 'first_name', 'last_name', 'image', 'date_created', 'date_modified', 'contacts')
        read_only_fields = ('date_created', 'date_modified')
