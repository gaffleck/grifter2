from rest_framework import serializers
from .models import Lot, Customer

class LotSerializer(serializers.ModelSerializer):
    """Serialize the lot"""

    class Meta:
        model = Lot
        fields = ('lot_num', 'lot_model_name', 'lot_model_desc', 'lot_inventoryid')

class CustomerSerializer(serializers.ModelSerializer):
    """Serialize the customer"""

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'customer_number')