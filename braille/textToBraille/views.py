from rest_framework import mixins, viewsets
from textToBraille.models import Translation
from textToBraille.serializer import TranslationSerializer


class TranslationViewSet(mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):
    
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()
    pass
