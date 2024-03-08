from django.db import models

# Create your models here.
class Participant (models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=8)
    password = models.CharField(max_length=8)
    def __str__(self):
        return self.name