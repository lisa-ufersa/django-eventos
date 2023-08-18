from django.contrib import admin
from eventos.models import Programacao

from users.models import Coordenador, Participante, Ministrante

# Register your models here.

admin.site.register(Coordenador)
admin.site.register(Participante)
admin.site.register(Ministrante)
