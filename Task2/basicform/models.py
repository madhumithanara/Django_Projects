from django.conf import settings
from django.db import models
from django.utils import timezone


class Applicant(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    whyme = models.TextField()
    ideas = models.TextField()

    def __str__(self):
        return self.name