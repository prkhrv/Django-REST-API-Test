from rest_framework import serializers
from .models import languages,paradigm,programmer

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = languages
        fields = ('url','id','name','paradigm')


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = paradigm
        fields = ('id','url','name')

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = programmer
        fields = ('id','url','name','languages')      
