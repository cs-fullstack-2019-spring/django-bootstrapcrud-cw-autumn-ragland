from django.db import models


# Item Model
class ItemModel(models.Model):
    name = models.CharField(max_length=500, default='')
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    imageURL = models.CharField(max_length=500, default='')
