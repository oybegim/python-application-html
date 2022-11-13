from django.db import models

class Odam(models.Model):
    ism = models.CharField(max_length=16)
    familiya = models.CharField(max_length=18)
    yosh = models.IntegerField(default=16)
    def __str__(self):
        return f"{self.ism} {self.familiya} {self.yosh}"

class Gul(models.Model):
    nomi = models.CharField(max_length=31)
    rangi = models.CharField(max_length=31)
    tarif = models.TextField(max_length=21)
    def __str__(self):
        return f"{self.nomi} {self.rangi} {self.tarif}"


class Hayvon(models.Model):
    nom = models.CharField(max_length=31)
    yosh=models.IntegerField(default=0)
    xulosa=models.TextField(max_length=31)
    def __str__(self):
        return f"{self.nom} {self.yosh} {self.xulosa}"


class Cola(models.Model):
    nom = models.CharField(max_length=21)
    muddat = models.IntegerField(default=1)
    tarif=models.TextField(max_length=31)
    def __str__(self):
        return f"{self.nom} {self.muddat} {self.tarif}"


class Kitkat(models.Model):
    gr = models.IntegerField(default=100)
    muddat = models.IntegerField(default=1)
    tarif=models.TextField(max_length=31)
    def __str__(self):
        return f"{self.gr} {self.muddat} {self.tarif}"


class Flash(models.Model):
    muddat = models.IntegerField(default=1)
    gr = models.IntegerField(default=250)
    xulosa=models.TextField(max_length=31)
    def __str__(self):
        return f"{self.muddat} {self.gr} {self.xulosa}"


class Suv(models.Model):
    nom = models.CharField(max_length=3)
    narx=models.IntegerField(default=2000)
    tarif=models.TextField(max_length=31)
    def __str__(self):
        return f"{self.nom} {self.narx} {self.tarif}"
