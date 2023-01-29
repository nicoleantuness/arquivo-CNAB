from django.db import models

# Create your models here.

class Types(models.Model):
    options_nature = [("Entrada", "Saída")]
    options_sinal = [("+", "-")]
    
    type = models.IntegerField()
    description = models.CharField(max_length=50)
    nature = models.CharField(max_length=8, choices=options_nature, default="Entrada")
    sinal = models.CharField(max_length=2,choices=options_sinal, default="+")
