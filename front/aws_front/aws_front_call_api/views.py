from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


HOST = 'http://127.0.0.1:8081'

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def home(request):
    data_rds = get_data_rds()
    context = {
        'data_rds': data_rds,
        'data_s3': data_rds
    }
    return HttpResponse(render(request, '../templates/home.html', context))

def get_data_rds():
    url = f"{HOST}/aws_api/matiere"
    response = requests.get(url)
    return response.json()

@csrf_exempt
def upload_rds(request):
    if request.method == 'POST':
        form = request.POST
        data = {
            "nom": form.get('nom'),
            "description": form.get('description'),
            "nb_heure": int(form.get('nb_heure')),
            "intervenant": form.get('intervenant')
        }
        url = f"{HOST}/aws_api/add_matiere"
        print(data)
        response = requests.post(url, json=data)
        if response.status_code == 200:
            messages.success(request, "Les données sont bien sauvegardé !")
        else:
            messages.error(request, "Erreur server!")
        return HttpResponseRedirect(reverse('index'))
