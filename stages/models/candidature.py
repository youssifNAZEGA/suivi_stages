from django.db import models

from stages.models.etudiant import Etudiant
from stages.models.offre import Offre


class Candidature(models.Model):
    date_candidate=models.DateField()
    etudiant=models.ForeignKey(Etudiant,related_name="candidature",on_delete=models.CASCADE)
    offre=models.ForeignKey(Offre,related_name="candidatures",on_delete=models.CASCADE)


    class Meta:
        ordering=["date_candidate"]
        verbose_name="Candidature"