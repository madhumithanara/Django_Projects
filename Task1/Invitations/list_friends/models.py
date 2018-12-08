from django.db import models

# Create your models here.

class Friend(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=2)
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)

    def __str__(self):
        return self.name


