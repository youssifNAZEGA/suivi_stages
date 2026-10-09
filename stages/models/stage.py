from django.db import models

from stages.models import Entreprise
from stages.models.enseignant_referent import EnseignantReference
from stages.models.etudiant import Etudiant
from stages.models.tuteur_entreprise import TuteurEntreprise



class Stage(models.Model):
    sujet=models.CharField()
    date_debut=models.DateField()
    date_fin=models.DateField(null=True)
    tuteur=models.OneToOneField(TuteurEntreprise,related_name="stage",on_delete=models.PROTECT)
    entreprise=models.OneToOneField(Entreprise,related_name="stage",on_delete=models.PROTECT)
    enseignants=models.ForeignKey(EnseignantReference,related_name="stages",on_delete=models.PROTECT)
    etudiants=models.ForeignKey(Etudiant,related_name="etudiants",on_delete=models.PROTECT)


    class Meta:
        ordering=["date_debut"]
        verbose_name="Stage"