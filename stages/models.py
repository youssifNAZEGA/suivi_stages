from django.db import models

# Create your models here.


class Entreprise(models.Model):


    nom=models.CharField(max_length=500, unique=True)

    ville=models.CharField(max_length=120)

    secteur=models.CharField(max_length=80)

    contact=models.EmailField(unique=True)

    logo=models.ImageField()
