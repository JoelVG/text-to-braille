from django.shortcuts import render
import rest_framework
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from .models import Translation
from rest_framework.response import Response
from .serializer import TranslationSerializer
from .py_braille import convert_text

#SECOND OPTION
# class TranslationView(viewsets.ModelViewSet):
#     serializer_class = TranslationSerializer
#     queryset = Translation.objects.all()

class TranslationView(APIView):
    
    serializer_class = TranslationSerializer
    
    def get(self, request):
        transcription = [ {"text": detail.text,"braille_translation": detail.detail} 
        for detail in Translation.objects.all()]
        return Response(transcription)
    
    
    def post(self, request):
        data = request.data
        return Response(convert_text(data['text']))
        