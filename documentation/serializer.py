from rest_framework import serializers
from .models import Types

class TypesSerializer(serializers.Serializer):
    type = serializers.CharField()
    description = serializers.CharField()
    nature = serializers.CharField(choices=Types.options_nature, default="Entrada")
    sinal = serializers.CharField(choices=Types.options_sinal, default="+")


    def create(self, validated_data):
        type = Types.objects.create(**validated_data)

        return type
    