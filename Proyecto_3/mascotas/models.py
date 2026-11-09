from django.db import models

class Responsable(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    correo = models.CharField(max_length=254, unique=True, null=False, blank=False)
    rut = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

class Mascota(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False) 
    anio_nacimiento = models.IntegerField(null=False, blank=False)
    especie = models.CharField(max_length=100, null=False, blank=False)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        return f"{self.nombre} - {self.especie}"