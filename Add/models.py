from django.db import models

# Create your models here.

class Add(models.Model):
    link=models.CharField(max_length=200, null=True)
    image=models.ImageField()
    active=models.IntegerField(null=True, blank=True, default=1)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link 
