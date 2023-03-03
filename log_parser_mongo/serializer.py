from rest_framework import serializers
from .models import LogParserMongo


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogParserMongo
        fields = ('id', 'vendor', 'device')
