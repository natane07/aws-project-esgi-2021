import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Matiere
import boto
import boto3

AWS_ACCESS_KEY = 'AKIAXL4VZJYZTK6AVZ4P'
AWS_SECRET_KEY = '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'
AWS_BUCKET_NAME = 'aws-project-esgi-test'

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

def download_file_s3(request):
    conn = boto.connect_s3(AWS_ACCESS_KEY, AWS_SECRET_KEY)
    bucket = conn.get_bucket(AWS_BUCKET_NAME)
    bucket_list = bucket.list()
    file_name_and_url_s3 = []
    for l in bucket_list:
        keyString = str(l.key)
        s3_url = f"https://{AWS_BUCKET_NAME}.s3.amazonaws.com/{keyString}"
        url_data = {
            "name": keyString,
            "url": s3_url
        }
        file_name_and_url_s3.append(url_data)

    data = {
        "succes": True,
        "file": file_name_and_url_s3
    }
    return JsonResponse(data)

@csrf_exempt
def upload_file_s3(request):
    conn = boto3.session.Session(AWS_ACCESS_KEY, AWS_SECRET_KEY)
    s3_resource = conn.resource('s3')
    bucket = s3_resource.Bucket(AWS_BUCKET_NAME)

    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        file_name = myfile.name
        bucket.put_object(Key=file_name, Body=myfile.read(), ACL='public-read')

    data = {
        "succes": True,
        "file": f"https://{AWS_BUCKET_NAME}.s3.amazonaws.com/{file_name}"
    }
    return JsonResponse(data)