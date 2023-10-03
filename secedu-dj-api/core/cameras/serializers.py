# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.cadastros.models import Aluno, Escalas
from core.cameras.models import NotaFiscal, Cameras, Locais, FrequenciasEscolar, Tarefas

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['nome', 'matricula']
    


class NotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaFiscal
        fields = ['id', 'numero', 'data']

class CamerasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cameras
        fields = ['id', 'descricao', 'acesso', 'modelo']

class LocaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locais
        fields = ['id', 'nome', 'descricao', 'camera', 'ponto']

class FrequenciasEscolarSerializer(serializers.ModelSerializer):
    #aluno = serializers.PrimaryKeyRelatedField(many=True, queryset=Aluno.objects.all())
    class Meta:
        model = FrequenciasEscolar
        fields = ['aluno', 'local' ,'data', ] 
class EscalasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escalas
        fields = '__all__'

class TarefasSerializer(serializers.ModelSerializer):
    escalas = EscalasSerializer()
    cameras = CamerasSerializer()

    class Meta:
        model = Tarefas
        fields = '__all__'
