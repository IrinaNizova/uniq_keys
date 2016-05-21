from .models import Key
from rest_framework import serializers

class KeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Key
        fields = ('status', 'value')

