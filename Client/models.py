from django.db import models

# Create your models here.

class Client(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200, null=True,blank=True)
    email=models.CharField(max_length=200, null=True, blank=True)
    ip=models.CharField(max_length=200, null=True, blank=True)
    geo_location=models.CharField(max_length=200, null=True, blank=True)
    active=models.IntegerField(null=True, blank=True, default=1)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 