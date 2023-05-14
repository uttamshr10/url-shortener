from django.db import models

# Create your models here.
class Link(models.Model):
    link = models.CharField(max_length=2000)
    uuid = models.CharField(max_length=15)
    def __str__(self):
        return self.link
