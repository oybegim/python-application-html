from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=16)
    familiya = models.CharField(max_length=16)


class Pepsi(models.Model):
    narx = models.IntegerField(default=5)
    litr = models.FloatField(default=0.5)
