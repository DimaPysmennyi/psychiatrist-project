from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    text = models.TextField()