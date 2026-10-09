from django.contrib import admin

from .models import (
    Entreprise,
    EnseignantReference,
    Etudiant,
    TuteurEntreprise,
    Offre,
    Competence,
    Candidature,
    Stage
)
# Register your models here.

@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ["nom","ville","secteur"]

    search_fields = ["nom","secteur","ville"]
@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display=["nom","prenom","sexe","date_naissance","email","matricule","promotion"]

    search_fields=["nom","prenom","promotion"]
@admin.register(EnseignantReference)
class EnseignantReferenceAdmin(admin.ModelAdmin):
    list_display=["nom","prenom","sexe","date_naissance","email","departement_pedagogique"]
    
    search_fields=["nom","prenom"]

@admin.register(TuteurEntreprise)
class TuteurEntrepriseAdmin(admin.ModelAdmin):
    list_display=["nom","prenom","sexe","date_naissance","email"]
        
    search_fields=["nom","prenom"]

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display=["libelle"]

    search_fields=["libelle"]


@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display=["intitule","description","date_debut","date_fin","nb_stagiaires"]

    search_fields=["intitule","date_debut","competence"]

@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display=["date_candidate","etudiant","offre"]

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display=["sujet","date_debut","date_fin","tuteur","entreprise","enseignants","etudiants"]