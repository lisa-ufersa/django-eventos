from django.db import models
from django.contrib.auth.models import User

from eventos.models import Evento, MiniEvento, Certificado

# Create your models here.

class UserProfileExample(models.Model):

    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=150)
    birth_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
    
    def __str__(self):
        return self.user.username

class Participante(models.Model):
    certificado = models.ManyToManyField(Certificado)
    frequencias = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"

    def __str__(self):
        return 

class Coordenador(models.Model):
    eventos = models.ForeignKey(Evento, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = "Coordenador"
        verbose_name_plural = "Coordenadores"

class Ministrante(models.Model):
    minieventos = models.ForeignKey(MiniEvento, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    class Meta:
        verbose_name = "Ministrante"
        verbose_name_plural = "Ministrantes"

class Voluntario(models.Model):
    eventos = models.ForeignKey(Evento, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    class Meta:
        verbose_name = "Voluntario"
        verbose_name_plural = "Voluntários"

class Patrocinador(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=100)
    eventos = models.ForeignKey(Evento, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    class Meta:
        verbose_name = "Patrocinador"
        verbose_name_plural = "Patrocinadores"
