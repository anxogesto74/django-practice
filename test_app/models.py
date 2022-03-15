from django.db import models

# Create your models here.

#SERÍA UNA CLASE
class Clase_prueba(models.Model):
    id = models.IntegerField(primary_key=True, default="auto_increment")
    nombre = models.CharField(max_length=30)
    email = models.EmailField()