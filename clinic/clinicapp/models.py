from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, default=None)
    email = models.EmailField()
    phone = PhoneNumberField()
    comment = models.TextField()