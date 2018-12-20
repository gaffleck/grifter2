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
    make = models.CharField(max_length=255, blank=True)
    model = models.CharField(max_length=255, blank=True)
    year = models.IntegerField(null=True)
    equipment_type = models.CharField(max_length=255, blank=True)
    shoot_price = models.IntegerField(null=True)
    on_watchlist = models.BooleanField(default=False)
    title = models.CharField(max_length=255, blank=True)
    thumbnail_image = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return "Asset {} {} {}".format(self.make, self.model, self.year)


class Image(models.Model):
    file_name = models.CharField(max_length=50)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return "image {}".format(self.fileName)


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
    asset = models.ForeignKey(Asset, related_name='conversations', on_delete=models.CASCADE)

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

class TwilioMessage(models.Model):
    """ A Twilio Message"""
    ApiVersion = models.CharField(max_length=100, blank=True, null=True)
    MessagingServiceSid = models.CharField(max_length=40, blank=True, null=True)
    SmsSid = models.CharField(max_length=40, blank=True, null=True)
    SmsStatus = models.CharField(max_length=40, blank=True, null=True)
    SmsMessageSid = models.CharField(max_length=40, blank=True, null=True)
    NumSegments = models.IntegerField( blank=True, null=True)
    From = models.CharField(max_length=40, blank=True, null=True)
    ToState = models.CharField(max_length=5, blank=True, null=True)
    MessageSid = models.CharField(max_length=40, blank=True, null=True)
    AccountSid = models.CharField(max_length=40, blank=True, null=True)
    ToZip = models.CharField(max_length=20, blank=True, null=True)
    FromCountry = models.CharField(max_length=100, blank=True, null=True)
    ToCity = models.CharField(max_length=100, blank=True, null=True)
    FromCity = models.CharField(max_length=100, blank=True, null=True)
    To = models.CharField(max_length=40, blank=True)
    FromZip = models.CharField(max_length=100, blank=True, null=True)
    Body = models.CharField(max_length=40, blank=True)
    ToCountry = models.CharField(max_length=100, blank=True, null=True)
    FromState = models.CharField(max_length=100, blank=True, null=True)
    NumMedia = models.IntegerField(blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='text_messages', null=True)





