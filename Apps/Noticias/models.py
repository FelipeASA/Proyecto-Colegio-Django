from django.db import models

# Create your models here.

class NoticiasModelo(models.Model):
    titulo=models.CharField(max_length=100)
    resumen=models.CharField(max_length=200)
    detalle=models.TextField(max_length=1000)
    fecha=models.DateField()
    tipo=models.CharField(max_length=50)
#     fecha=models.date()   tipo{}

      

    def __str__(self):
        return self.nombre
