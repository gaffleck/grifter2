from rest_framework import serializers
from .models import Lot, Customer, Sale

class LotSerializer(serializers.ModelSerializer):
    """Serialize the lot"""

    class Meta:
        model = Lot
        fields = ('lot_num', 'lot_model_name', 'lot_model_desc', 'lot_inventoryid', 'lot_bidder_number', 'lot_equipment_code', 'lot_equipment_type', 'lot_equipment_sub_type', 'lot_sold_price',\
            'lot_shoot_price', 'lot_inyard_date', 'lot_checkout_date', 'lot_photo', 'lot_asset_guid')

class CustomerSerializer(serializers.ModelSerializer):
    """Serialize the customer"""

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'customer_number')

class SaleSerializer(serializers.ModelSerializer):
    """Serialize the sale"""

    class Meta:
        model = Sale
        fields = ('sale_number', 'sale_office', 'sale_date')