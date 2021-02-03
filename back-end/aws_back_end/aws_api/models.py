from django.db import models

class Matiere(models.Model):
    nom = models.CharField(max_length=300)
    nb_heure = models.FloatField()
    intervenant = models.CharField(max_length=300)
    description = models.TextField()
    class Meta:
       managed = False
       db_table = 'matiere'
