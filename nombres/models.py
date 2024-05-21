from django.db import models

# Create your models here.


class Region(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nom}"


class CoordinationLocale(models.Model):
    nom = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom}"


class Jeune(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    coordination_locale = models.ForeignKey(CoordinationLocale, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} {self.coordination_locale}"


class MembreBureauRegional(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} {self.region}"




