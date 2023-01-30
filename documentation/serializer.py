from rest_framework import serializers
from .models import Types
import ipdb

class TypesSerializer(serializers.Serializer):
    class Meta:
        model = Types
        fields = '__all__'

    
    
    def create(self, validated_data):
        # ipdb.set_trace()
        return Types.objects.create(**validated_data)
    