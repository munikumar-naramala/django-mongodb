from rest_framework import serializers
from logmongo.models import Logmongo


class LogmongoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logmongo
        fields = ('id',
                  'title',
                  'description',
                  'published')