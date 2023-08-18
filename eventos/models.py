from django.db import models


# Create your models here.
class MiniEvento(models.Model):
    titulo = models.CharField(max_length=150) 
    descricao = models.CharField(max_length=400)
    carga_horaria = models.IntegerField()
    horario = models.TimeField()
    local = models.CharField(max_length=150)

class Certificado(models.Model):
    minievento = models.ForeignKey(MiniEvento, on_delete=models.CASCADE)

class Programacao(models.Model):
    minieventos = models.ForeignKey(MiniEvento, on_delete=models.CASCADE)

class Evento(models.Model):
    nome = models.CharField(max_length=150)
    data = models.DateField()
    local = models.CharField(max_length=150)
    programacao = models.ForeignKey(Programacao, on_delete=models.CASCADE)

