from django.db import models

# Create your models here.

class Types(models.Model):
    type = models.IntegerField()
    date = models.DateField()
    value = models.DecimalField(max_digits=12, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=20)
    hour = models.TimeField()
    owner_store = models.CharField(max_length=20)
    store_name = models.CharField(max_length=20)

    def __repr__(self):
        return f"{self.type} - {self.date} - {self.value} - {self.cpf} - {self.card} - {self.hour} - {self.owner_store} - {self.store_name}"