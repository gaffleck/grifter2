from django.db import models
import uuid


#can we rename the class without changing table?
class Lot(models.Model):
    """ lot table"""
    lot_num = models.IntegerField(null=True)
    lot_model_name = models.CharField(max_length=15, null=True)
    lot_model_desc = models.CharField(max_length=35, null=True)
    lot_inventoryid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        db_table = 'GA_Lot'


    def __str__(self):
        """string defn of class"""
        return '{} {} '.format(self.lot_model_name, self.lot_model_desc)
