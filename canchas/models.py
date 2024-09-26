from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Cancha(models.Model):
    numero_cancha = models.IntegerField()
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"Cancha {self.numero_cancha} - {self.nombre}"

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"Reserva de {self.usuario} en {self.cancha} de {self.hora_inicio} a {self.hora_fin}"

