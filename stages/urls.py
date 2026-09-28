from django.urls import path
from . import views


app_name="stages"

urlpatterns = [
    path("entreprises/", views.list_entreprise, name="liste_entreprises"),
]