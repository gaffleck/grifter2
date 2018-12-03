# api/serializers.py

from rest_framework import serializers
from .models import Customer, Friend

   
class FriendSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Friend
        fields = ('id', 'name', 'date_created', 'date_modified','customer')
        read_only_fields = ('date_created', 'date_modified')
        depth = 1

class FriendSubSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Friend
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
        


       


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    #friends = serializers.PrimaryKeyRelatedField(many=True, read_only=False,queryset=Friend.objects.all())
    friends = FriendSubSerializer(required=False,many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Customer
        fields = ('id', 'name', 'date_created', 'date_modified','friends')
        read_only_fields = ('date_created', 'date_modified')
    
