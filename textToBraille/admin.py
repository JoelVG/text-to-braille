from django.contrib import admin
from .models import Translation
# Register your models here.

class TranslationAdmin(admin.ModelAdmin):
    list_display = ('text', 'braille_translation')

admin.site.register(Translation, TranslationAdmin)