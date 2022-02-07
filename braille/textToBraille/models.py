from django.db import models
from textToBraille.py_braille import convert_text

class Translation(models.Model):
    text = models.CharField(max_length=1000)
    braille_translation = models.CharField(max_length=3000, blank=True)
    
    def __str__(self):
        return self.text    
    
    def save(self, *args, **kwargs):
        self.text = self.text
        self.braille_translation = convert_text(self.text)
        super(Translation, self).save(*args, **kwargs)