from django.db import models


class Competence(models.Model):

    libelle=models.CharField()

    class Meta:
        verbose_name='Competence'