from rest_framework import serializers
from users.models import UserProfileExample, Coordenador, Ministrante, Participante, Voluntario, Patrocinador

class UserProfileExampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfileExample
        fields = ['id', 'address', 'phone_number', 'birth_date', 'user']

class ParticipanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participante
        fields = ['id', 'certificado', 'frequencias', 'user']

class CoordenadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coordenador
        fields = ['id', 'eventos', 'user']

class MinistranteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ministrante
        fields = ['id', 'minieventos','user' ]

class VoluntarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Voluntario
        fields = ['id','eventos','user']

class PatrocinadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patrocinador
        fields = ['id', 'nome', 'cnpj', 'eventos', 'user']