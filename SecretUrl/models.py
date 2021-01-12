from django.db import models

# Create your models here.
class SecretUrl(models.Model):
    url_hash = models.CharField("Url", blank=False, max_length=250, unique=True)
    expires = models.DateTimeField("Expires")