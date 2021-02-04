from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('matiere', views.get_matiere_rds, name='matiere'),
    path('add_matiere', views.add_matiere_rds, name='add_matiere'),
    path('download_file', views.download_file_s3, name='download_file'),
    path('upload_file', views.upload_file_s3, name='download_file'),
]