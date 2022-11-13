from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=16)
    familiya = models.CharField(max_length=16)
    