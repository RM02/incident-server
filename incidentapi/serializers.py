from rest_framework import serializers
from incidentapi.models import Incident

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ("id", "incident", "incident_type", "status", "description", "created_date", "updated_date", "created_by", "updated_by")