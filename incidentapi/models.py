from django.db import models
from uuid import uuid4

class Incident(models.Model):
    id = models.CharField(primary_key=True, default=uuid4(), max_length=200, auto_created=True)
    incident = models.CharField(max_length=250)
    #priority = models.CharField(max_length=200, choices=[("Alta", "Alta"), ("Media", "Media"), ("Baja", "Baja")])
    status = models.CharField(max_length=500, auto_created=True, default="En proceso", choices=[("En proceso", "En proceso"), ("Descartada", "Descartada"), ("Verificado", "Verificado")])
    incident_type = models.CharField(max_length=250, choices=[("Derrame", "Derrame"), ("Incendio", "Incendio"), ("Caida", "Caida")])
    description = models.CharField(max_length=250)

    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(max_length=250, default='admin', auto_created=True)
    updated_by = models.CharField(max_length=250, default='admin', auto_created=True)

