from rest_framework import viewsets
from farmacia.models import Cliente
from farmacia.serializer import ClienteSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

