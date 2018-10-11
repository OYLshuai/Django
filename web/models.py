from django.db import models

# Create your models here.

class text(models.Model):
     id = models.BigIntegerField
     name = models.CharField(max_length=20, default='a')
     age = models.IntegerField(null=True)
