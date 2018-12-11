from django.db import models
import uuid



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



class Customer(models.Model):
    """ customer table"""
    first_name = models.CharField(null=True, max_length=75, db_column='CST_F_NAME')
    last_name = models.CharField(null=True, max_length=75, db_column='CST_L_NAME')
    customer_number = models.IntegerField(primary_key=True, db_column='CST_RBANUM')

    class Meta:
        db_table = 'GA_Customer'


    def __str__(self):
        """string defn of class"""
        return '{} {} '.format(self.first_name, self.last_name)
