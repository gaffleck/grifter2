"""models class"""
from django.db import models


class Customer(models.Model):
    """ Customer Model Class"""
    first_name = models.CharField(max_length=255, blank=False, unique=False)
    last_name = models.CharField(max_length=255, blank=False, unique=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.first_name)

class Friend(models.Model):
    """Friends Model Class"""
    first_name = models.CharField(max_length=255, blank=False, unique=False)
    last_name = models.CharField(max_length=255, blank=False, unique=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, related_name='friends', on_delete=models.CASCADE)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.first_name)

class Gift(models.Model):
    """Gift Model Class """
    gift_name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{}".format(self.gift_name)

class GiftRecord(models.Model):
    """Record of a gift given"""
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    price = models.IntegerField()
    date_given = models.DateTimeField()
    friend = models.ForeignKey(Friend, related_name='gift_history', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.gift.gift_name)

class GiftSuggestion(models.Model):
    """Gift Suggestion Class """
    date_suggested = models.DateTimeField(auto_now=True)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)

    def __str__(self):
        return "gift suggestion of {0}".format(self.gift.gift_name)
