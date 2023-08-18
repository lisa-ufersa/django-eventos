from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from users.api.serializers import MinistranteSerializer, UserProfileExampleSerializer, ParticipanteSerializer, CoordenadorSerializer

from users.models import Coordenador, Ministrante, Participante, UserProfileExample

class UserProfileExampleViewSet(ModelViewSet):
    serializer_class = UserProfileExampleSerializer
    permission_classes = [AllowAny]
    queryset = UserProfileExample.objects.all()
    http_method_names = ['get', 'put']

class ParticipanteViewSet(ModelViewSet):
    serializer_class = ParticipanteSerializer
    permission_classes = [AllowAny]
    queryset = Participante.objects.all() # SELECT * FROM participantes;

class CoordenadorViewSet(ModelViewSet):
    serializer_class = CoordenadorSerializer
    permission_classes = [AllowAny]
    queryset = Coordenador.objects.all()

class MinistranteViewSet(ModelViewSet):
    serializer_class = MinistranteSerializer
    permission_classes = [AllowAny]
    queryset = Ministrante.objects.all()