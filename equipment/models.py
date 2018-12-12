from django.db import models
import uuid



class Lot(models.Model):
    """ lot table"""
    lot_num = models.IntegerField(null=True)
    lot_model_name = models.CharField(max_length=15, null=True)
    lot_model_desc = models.CharField(max_length=35, null=True)
    lot_inventoryid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lot_bidder_number = models.IntegerField(null=True, db_column='lot_bidnum')
    lot_equipment_code = models.CharField(max_length=5, null=True, db_column='lot_eqgrpcode')
    lot_equipment_type = models.CharField(max_length=5, null=True, db_column='lot_eqtype')
    lot_equipment_sub_type = models.CharField(max_length=5, null=True, db_column='lot_eqsubtype')
    lot_sold_price = models.DecimalField(db_column='lot_soldprice', max_digits=13, decimal_places=2, null=True)
    lot_shoot_price = models.DecimalField(db_column='lot_shootprice', max_digits=13, decimal_places=2, null=True)
    lot_inyard_date = models.DateField()
    lot_checkout_date = models.DateField()
    lot_photo = models.CharField(db_column='lot_eei_asset_photo_filename', null=True, max_length=48)
    lot_asset_guid = models.UUIDField(editable=False)




    class Meta:
        db_table = 'GA_Lot'


    def __str__(self):
        """string defn of class"""
        return '{} {} '.format(self.lot_model_name, self.lot_model_desc)



class Customer(models.Model):
    """ customer table"""
    first_name = models.CharField(null=True, max_length=75, db_column='CST_F_NAME')
    last_name = models.CharField(null=True, max_length=75, db_column='CST_L_NAME')
    title = models.CharField(null=True, max_length=75, db_column='CST_TITLE')
    customer_number = models.IntegerField(primary_key=True, db_column='CST_RBANUM')
    sale_number = models.IntegerField(db_column='CST_SALENUM')
    company_name = models.CharField(db_column='CST_CONAME', max_length=150)
    bidder_number = models.IntegerField(db_column='CST_BIDNUM', null=False)
    country = models.CharField(db_column='CST_COUNTRY', max_length=3)
    purchase_threshold = models.DecimalField(db_column='CST_PUR_THRESHOLD', max_digits=13, decimal_places=2, null=True)
    customer_type = models.CharField(max_length=3, db_column='CST_CUSTOMER_TYPE')

    class Meta:
        db_table = 'GA_Customer'


    def __str__(self):
        """string defn of class"""
        return '{} {} '.format(self.first_name, self.last_name)

class Sale(models.Model):
    """ Sale table"""
    sale_number = models.IntegerField(null=False, primary_key=True, db_column='SV_SALENUM')
    sale_office = models.CharField(null=True, max_length=50, db_column='SV_OFFICE')
    sale_date = models.DateField(db_column='SV_SALEDATE')
    sale_days = models.IntegerField(db_column='SV_SALEDAYS')
    sale_address = models.CharField(db_column='SV_ADDR1', max_length=30)
    sale_address_2 = models.CharField(db_column='SV_ADDR2', max_length=30)
    sale_city = models.CharField(db_column='SV_CITY', max_length=30)
    sale_province = models.CharField(db_column='SV_PROV', max_length=25)
    sale_country = models.CharField(db_column='SV_COUNTRY', max_length=25)
    


    class Meta:
        db_table = 'GA_SaleVars'


    def __str__(self):
        """string defn of class"""
        return 'sale {} '.format(self.sale_number)
