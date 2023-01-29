from django.db import models

# Create your models here.

class Types(models.Model):
    options_nature = [("Entrada", "Saída")]
    options_sinal = [("+", "-")]
    
    type = models.IntegerField()
    description = models.CharField()
    nature = models.CharField(choices=options_nature, default="Entrada")
    sinal = models.CharField(choices=options_sinal, default="+")
