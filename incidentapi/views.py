from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from incidentapi.serializers import IncidentSerializer
from incidentapi.models import Incident


class IncidentView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'incident', 'status']
