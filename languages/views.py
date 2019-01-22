from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import languages,paradigm,programmer
from .serializers import LanguageSerializer,ParadigmSerializer,ProgrammerSerializer
# Create your views here.

class LanguageView(viewsets.ModelViewSet):
    queryset = languages.objects.all()
    serializer_class = LanguageSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ParadigmView(viewsets.ModelViewSet):
    queryset = paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = ProgrammerSerializer
