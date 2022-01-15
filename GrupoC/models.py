from django.db import models

class Cerveza(models.Model):
    
    nombre=models.CharField('nombre', max_length=40)
    IBU=models.IntegerField()
    grad_alcohol=models.FloatField()
    
