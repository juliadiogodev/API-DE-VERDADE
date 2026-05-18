from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Genero, Filme
from .serializers import GeneroSerializer, FilmeSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer



class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all().order_by('titulo')
    serializer_class = FilmeSerializer