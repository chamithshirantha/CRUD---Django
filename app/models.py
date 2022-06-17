from django.db import models

# Create your models here.

class Info(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    mobile = models.IntegerField(max_length=10)