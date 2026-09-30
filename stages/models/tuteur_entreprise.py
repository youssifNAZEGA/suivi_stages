from django.db import models

from stages.models.personne import Personne

class TuteurEntreprise(Personne):
    nom_entreprise=models.CharField()
    poste=models.CharField()


    class Meta(Personne.Meta):
        verbose_name="Tuteur d'entreprise"