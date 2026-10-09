from django.db import models



class Personne(models.Model):


    nom = models.CharField(max_length=500)
    prenom = models.CharField(max_length=500)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=1)
    email = models.EmailField()

    class Meta:
        abstract = True