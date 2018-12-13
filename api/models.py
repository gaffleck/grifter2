"""models class"""
from django.db import models
import logging 

logger = logging.getLogger(__name__)


class User(models.Model):
    """ Customer Model Class"""
    first_name = models.CharField(max_length=255, blank=False, unique=False)
    middle_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False, unique=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=255, blank=True, unique=False)
    phone_number = models.CharField(max_length=20, blank=False)

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
    industry = models.CharField(max_length=255, blank=True)
    quality = models.IntegerField()
    phone_number = models.CharField(max_length=20, blank=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.first_name)

class Note(models.Model):
    """ customer notes"""
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=1000)
    contact = models.ForeignKey(Contact, related_name='notes', on_delete=models.CASCADE)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.content)


class Asset(models.Model):
    """Asset Class """
    make = models.CharField(max_length=255, blank=False)
    model = models.CharField(max_length=255, blank=False)
    year = models.IntegerField(blank=True)
    equipment_type = models.CharField(max_length=255, blank=False)
    shoot_price = models.IntegerField(blank=True)


    def __str__(self):
        return "Asset {} {} {}".format(self.make, self.model, self.year)

class Purchase(models.Model):
    """An asset purchase"""
    price = models.DecimalField(decimal_places=2, max_digits=13)
    contact = models.ForeignKey(Contact, related_name='purchases', on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, related_name='asset', on_delete=models.CASCADE)

    def __str__(self):
        return "Purchase {} {} {}".format(self.asset.make, self.asset.model, self.price)


class Conversation(models.Model):
    """ a conversation"""
    user = models.ForeignKey(User, related_name='conversations', on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, related_name='conversations', on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

    def __str__(self):
        return "Conversation between {} and {} ".format(self.user.first_name, self.contact.first_name)

class Message(models.Model):
    """Send a message"""
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=1000, blank=False)
    message_status = models.CharField(max_length=100, blank=False, default='UNSENT')
    

    def __str__(self):
        return "Message {} ".format(self.message)







