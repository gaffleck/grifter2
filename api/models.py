"""models class"""
from django.db import models
import logging 

logger = logging.getLogger(__name__)


class User(models.Model):
    """ Customer Model Class"""
    first_name = models.CharField(max_length=255, blank=False, unique=False)
    last_name = models.CharField(max_length=255, blank=False, unique=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=255, blank=True, unique=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.first_name)

class Contact(models.Model):
    """Friends Model Class"""
    first_name = models.CharField(max_length=255, blank=False, unique=False)
    last_name = models.CharField(max_length=255, blank=False, unique=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
    image = models.CharField(max_length=255, blank=True, unique=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.first_name)

class SpecialDateType(models.Model):
    """types of special Dates"""
    date_type = models.CharField(max_length=255, blank=False)

    def __str__(self):
        """types of special date"""
        return "{}".format(self.date_type)


class SpecialDate(models.Model):
    """Special Dates Class"""
    contact = models.ForeignKey(Contact, related_name='special_dates', on_delete=models.CASCADE)
    date = models.DateField()
    date_type = models.ForeignKey(SpecialDateType, on_delete=models.CASCADE)


    def __str__(self):
        """return a human readable representation"""
        return 'Special date for {} of {}'.format(self.contact.first_name, self.date)


class Gift(models.Model):
    """Gift Model Class """
    gift_name = models.CharField(max_length=255, blank=False)
    gift_description = models.CharField(max_length=1000, blank=True)
    source = models.CharField(max_length=255, blank=False)
    image = models.CharField(max_length=255, blank=True, unique=False)


    def __str__(self):
        return "{}".format(self.gift_name)

class GiftRecord(models.Model):
    """Record of a gift given"""
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    price = models.IntegerField()
    date_given = models.DateTimeField()
    contact = models.ForeignKey(Contact, related_name='gift_history', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.gift.gift_name)

class GiftSuggestion(models.Model):
    """Gift Suggestion Class """
    date_suggested = models.DateTimeField(auto_now=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)

    def __str__(self):
        return "gift suggestion of {0}".format(self.gift.gift_name)

class Asset(models.Model):
    """Asset Class """
    make = models.CharField(max_length=255, blank=False)
    model = models.CharField(max_length=255, blank=False)
    year = models.IntegerField(blank=True)
    equipment_type = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "Asset {} {} {}".format(self.make, self.model, self.year)


