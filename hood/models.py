from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from pyuploadcare.dj.models import ImageField

class NeighbourHood(models.Model):
    name  = models.CharField(max_length=90)
    location =models.CharField(max_length=800)
    hood_logo = models.ImageField(upload_to="images",default="test.png")
    description = models.TextField()
    health_contact = models.IntegerField(blank=True,null=True)
    police_contact =  models.IntegerField(blank=True,null=True)
    admin = models.ForeignKey("Profile",on_delete=models.CASCADE,related_name="hood")


    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def __str__(self):
        return f"{self.name}"



# Create your models here.
