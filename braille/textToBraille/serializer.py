from rest_framework import serializers
from textToBraille.models import Translation
  
class TranslationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Translation
        fields = ('id', 'text', 'braille_translation')
        read_only_fields  = ['braille_translation']