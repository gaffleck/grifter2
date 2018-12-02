
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class Friend(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
