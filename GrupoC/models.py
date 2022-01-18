from django.db import models

class Cerveza(models.Model):
    
    nombre=models.CharField('nombre', max_length=40)
    IBU=models.IntegerField()
    grad_alcohol=models.FloatField()

    def __str__ (self):
        return self.nombre
    
class Cerveceria(models.Model):
    
    nombre=models.CharField('nombre', max_length=40)
    dire=models.CharField('dire', max_length=40)

    def __str__ (self):
        return self.nombre
class Experiencia(models.Model):
    
    nombre=models.CharField('nombre', max_length=40)
    apellido=models.CharField('apellido', max_length=40)
    cerv_tomada=models.CharField('cervezaTomada', max_length=40)
    cerv_atend=models.CharField('cervezaAtendida', max_length=40)
    punt_cerveza=models.IntegerField()
    punt_cerveceria=models.IntegerField()

    def __str__ (self):
        return self.nombre
    