from django.db import models

class Translation(models.Model):
    text = models.CharField(max_length=1000)
    braille_translation = models.CharField(max_length=3000)
    
    def __str__(self):
        return self.text