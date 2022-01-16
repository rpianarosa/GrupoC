from django.db import models

class Cerveza(models.Model):
    
    nombre=models.CharField('nombre', max_length=40)
    IBU=models.IntegerField()
    grad_alcohol=models.FloatField()
    
class Cerveceria(models.Model):
    
    nombre=models.CharField('nombre', max_length=40)
    dire=models.CharField('dire', max_length=40)
class Experiencia(models.Model):
    
    nombre=models.CharField('nombre', max_length=40)
    apellido=models.CharField('apellido', max_length=40)
    exp=models.CharField('exp', max_length=50)
    