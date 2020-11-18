from django.db import models

# Create your models here.

class ItemsList(models.Model):
    itemname = models.CharField(max_length=100)
    itemprice = models.IntegerField()
