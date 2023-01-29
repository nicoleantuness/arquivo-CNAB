from rest_framework import serializers
from .models import Types
import ipdb

class TypesSerializer(serializers.Serializer):
    type = serializers.IntegerField()
    date = serializers.DateTimeField()
    value = serializers.DecimalField(max_digits=12, decimal_places=2)
    cpf = serializers.CharField(max_length=11)
    card = serializers.CharField(max_length=20)
    hour = serializers.TimeField()
    owner_store = serializers.CharField(max_length=20)
    store_name = serializers.CharField(max_length=20)

    
    
    def create(self, validated_data):
        # ipdb.set_trace()
        return Types.objects.create(**validated_data)
    