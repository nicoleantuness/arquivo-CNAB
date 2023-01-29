from rest_framework import serializers
from .models import Types
import ipdb

class TypesSerializer(serializers.Serializer):
    type = serializers.IntegerField()
    description = serializers.CharField(max_length=50)
    nature = serializers.ChoiceField(choices=Types.options_nature, default="Entrada")
    sinal = serializers.ChoiceField(choices=Types.options_sinal, default="+")

    
    
    def create(self, validated_data):
        # ipdb.set_trace()
        return Types.objects.create(**validated_data)
    