from django.db import models

class Steep(models.Model):
    tam = models.CharField(max_length=21)
    gr = models.IntegerField(default=31)
    xulosa = models.TextField(max_length=31)
    def __str__(self):
        return f"{self.tam} {self.gr} {self.xulosa}"


class RedBull(models.Model):
    gr = models.IntegerField(default=250)
    enetgetik =models.TextField(max_length=31)
    tam=models.TextField(max_length=31)
    def __str__(self):
        return f"{self.gr} {self.energetik} {self.tam}"



class Nesquik(models.Model):
    nom = models.CharField(max_length=21)
    tam = models.TextField(max_length=31)
    gr = models.IntegerField(default=200)
    def __str__(self):
        return f"{self.nom} {self.tam} {self.gr}"

    
class Mirinda(models.Model):
    nom =models.CharField(max_length=21)
    tam=models.TextField(max_length=31)
    def __str__(self):
        return f"{self.nom} {self.tam}"


class Meva(models.Model):
    nom = models.CharField(max_length=31)
    kg = models.IntegerField(default=1)
    tam = models.TextField(max_length=21)
    def __str__(self):
        return f"{self.nom} {self.kg} {self.tam}"


class Lavash(models.Model):
    nom = models.CharField(max_length=21)
    narx = models.IntegerField(default=23)
    tam = models.TextField(max_length=31)
    def __str__(self):
        return f"{self.nom} {self.narx} {self.tam}"