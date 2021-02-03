from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('matiere', views.get_matiere_rds, name='matiere'),
    path('add_matiere', views.add_matiere_rds, name='add_matiere'),
]