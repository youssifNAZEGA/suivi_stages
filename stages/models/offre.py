from django.db import models

from stages.models.competence import Competence


class Offre(models.Model):
    intitule=models.CharField()
    description=models.TextField()
    date_debut=models.DateField()
    date_fin=models.DateField()
    nb_stagiaires=models.IntegerField()
    competence=models.ManyToManyField(Competence,related_name="offres")

    class Meta:
        verbose_name='Offre de stage'