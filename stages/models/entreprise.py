from django.db import models

from stages.models.tuteur_entreprise import TuteurEntreprise

# Create your models here.


class Entreprise(models.Model):


    nom=models.CharField(max_length=500, unique=True)

    ville=models.CharField(max_length=120)

    secteur=models.CharField(max_length=80)

    contact=models.EmailField(unique=True)

    logo=models.ImageField()

    tuteur=models.ForeignKey(TuteurEntreprise,related_name="entreprise",on_delete=models.CASCADE)


    class Meta:
        ordering=["nom"]
        verbose_name="Entreprise"

    def __str__(self):
        return f"{self.nom} ({self.ville})"