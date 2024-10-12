from django.db import models

# Create your models here.
class Inventory(models.Model):
    item_id=models.IntegerField()
    name=models.CharField(max_length=255)
    discription=models.CharField(max_length=255)