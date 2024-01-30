from rest_framework import mixins, viewsets, status
from django.http import JsonResponse
from textToBraille.models import Translation
from textToBraille.serializer import TranslationSerializer
from textToBraille.utils.py_braille import convert_file


class TranslationViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()

    def convert_file(self, request):
        """
        Función que recibe el path de un archivo .txt o .pdf
        y retorna la transcripción del mismo
        """
        if (file_path := request.POST.get("text")) is not None:
            text_converted = convert_file(file_path)
        else:
            return JsonResponse(
                data={"error": "No se ha encontrado el archivo"},
                status=status.HTTP_404_NOT_FOUND,
            )

        data = {"text": file_path, "braille_translation": text_converted}
        return JsonResponse(data=data, status=status.HTTP_200_OK)
