from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from eventos.api.serializers import CertificadoSerializer, EventoSerializer, MiniEventoSerializer, ProgramacaoSerializer

from eventos.models import Certificado, Evento, MiniEvento, Programacao

class MinieventoViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = MiniEvento.objects.all()
    serializer_class = MiniEventoSerializer

class EventoViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class ProgramacaoViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Programacao.objects.all()
    serializer_class = ProgramacaoSerializer

class CertificadoViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer