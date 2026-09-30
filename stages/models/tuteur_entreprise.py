from django.db import models

from stages.models.personne import Personne

class TuteurEntreprise(Personne):


    class Meta(Personne.Meta):
        verbose_name="Tuteur d'entreprise"