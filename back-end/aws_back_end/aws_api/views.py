import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Matiere



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_matiere_rds(request):
    return JsonResponse(
        list(Matiere.objects.all().order_by("id").values()),
        safe=False,
        json_dumps_params={'ensure_ascii': False}
    )

@csrf_exempt
def add_matiere_rds(request):
    succes = True
    if request.method == 'POST':
        data = json.loads(request.body)
        nom = data['nom'] if 'nom' in data else None
        description = data['description'] if 'description' in data else None
        nb_heure = data['nb_heure'] if 'nb_heure' in data else 0
        nb_heure = nb_heure if type(nb_heure) == int or type(nb_heure) == float else 0
        intervenant = data['intervenant'] if 'intervenant' in data else None

        new_matiere = Matiere(
            nom=nom,
            description=description,
            nb_heure=nb_heure,
            intervenant=intervenant
        )
        new_matiere.save()
    else:
        succes = False

    data = {
        "succes": succes
    }
    return JsonResponse(data)
