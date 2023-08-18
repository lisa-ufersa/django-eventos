from rest_framework.serializers import ModelSerializer

from eventos.models import Evento, MiniEvento, Certificado, Programacao

class MiniEventoSerializer(ModelSerializer):
    class Meta:
        model = MiniEvento
        fields = ['id','titulo', 'descricao', 'carga_horaria', 'horario', 'local']

class CertificadoSerializer(ModelSerializer):
    class Meta:
        model = Certificado
        fields = ['id', 'minievento']

class ProgramacaoSerializer(ModelSerializer):

    class Meta:
        model = Programacao
        fields = ['id','minieventos']

class EventoSerializer(ModelSerializer):

    class Meta:
        model = Evento
        fields = ['id','nome','data', 'local', 'programacao']