
from django.shortcuts import render

from stages.models import Entreprise

# Create your views here.

def list_entreprise(request):
    entreprises = Entreprise.objects.all()


    return render(
        request,
        "stages/liste_entreprises.html",
        {"entreprises":entreprises}
    )