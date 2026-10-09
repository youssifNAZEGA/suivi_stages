from django.db import models

from stages.models.competence import Competence
from stages.models.personne import Personne



class Etudiant(Personne):
    matricule= models.CharField()
    promotion = models.CharField()
    competence=models.ManyToManyField(Competence,related_name="etudiants")

    class Meta(Personne.Meta):
        verbose_name='Etudiant'