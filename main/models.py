from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.CharField(max_length=2000)
    url_id = models.CharField(max_length=15)
