from rest_framework import mixins, viewsets
from django.http import HttpResponse
from textToBraille.models import Translation
from textToBraille.serializer import TranslationSerializer
from textToBraille.utils.py_braille import convert_file


class TranslationViewSet(mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):
    
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()
    
    
    def convert_file(self, request):
        '''
        Función que recibe el path de un archivo .txt o .pdf
        y retorna la transcripción del mismo
        '''
        file = request.POST.get('text')
        if file is not None:
            text_converted = convert_file(file)
        else:
            return file
        return HttpResponse(text_converted)
