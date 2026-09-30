from django.db import models

from stages.models.personne import Personne



class Etudiant(Personne):
    cls_promotion = models.CharField()

    cv = models.FilePathField()


    class Meta(Personne.Meta):
        verbose_name='Livre'