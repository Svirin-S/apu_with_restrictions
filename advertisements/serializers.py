from rest_framework import serializers

from .models import *


class AdvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = ['id', 'user', 'text', 'created_at', 'open']
        read_only_fields = ['user']

