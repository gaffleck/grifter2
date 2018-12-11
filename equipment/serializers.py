from rest_framework import serializers
from .models import Lot

class LotSerializer(serializers.ModelSerializer):
    """Serialize the gift"""

    class Meta:
        model = Lot
        fields = ('lot_num', 'lot_model_name', 'lot_model_desc', 'lot_inventoryid')