from django.db import models

class Cerveza(models.Model):
    
    nombre=models.CharField('nombre', max_length=40)
    IBU=models.IntegerField()
    grad_alcohol=models.FloatField('ABV (%)')

    def __str__ (self):
        return self.nombre
    
class Cerveceria(models.Model):
    
    nombre=models.CharField('Nombre', max_length=40)
    dire=models.CharField('Barrio', max_length=40)

    def __str__ (self):
        return self.nombre
class Experiencia(models.Model):
    
    nombre=models.CharField('Nombre',null=True, max_length=40)
    apellido=models.CharField('Apellido', null=True, max_length=40)
    cerv_tomada= models.CharField('¿Que cerveza tomaste?',null=True, max_length=40)
    cerv_atend=models.CharField('¿A cual cerveceria fuiste?', null=True, max_length=40)
    punt_cerveza=models.IntegerField('Puntaje Cerveza', null=True)
    punt_cerveceria=models.IntegerField('Puntaje Cerveceria', null=True)
    
    def __str__ (self):
        return f' {self.nombre} {self.apellido}'