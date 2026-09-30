from django.db import models

from stages.models.personne import Personne


class EnseignantReference(Personne):
    departement_pedagogique=models.CharField()


    class Meta(Personne.Meta):
        verbose_name="Enseignant de reference"