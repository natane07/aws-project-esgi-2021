from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='index'),
    path('upload_rds', views.upload_rds, name='upload_rds'),
    path('upload_s3', views.upload_s3, name='upload_s3'),
]