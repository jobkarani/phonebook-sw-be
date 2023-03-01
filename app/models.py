from django.db import models
from django.urls import reverse
from pyuploadcare.dj.models import ImageField
# Create your models here.

class Contact(models.Model):
    firstName = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=256, unique=True)
    phoneNumber = models.IntegerField(max_length=200, null=True)
    profilePicture = ImageField( manual_crop="")
    location = models.CharField(max_length=200, null=True)

    class Meta:
        ordering = ('firstName',)

    def __str__(self):
        return self.firstName
    
