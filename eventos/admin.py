from django.contrib import admin

from eventos.models import Evento, MiniEvento, Programacao, Certificado

# Register your models here.

admin.site.register(Evento)
admin.site.register(MiniEvento)
admin.site.register(Programacao)
admin.site.register(Certificado)