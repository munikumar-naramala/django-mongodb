from django.db import models


class LogParserMongo(models.Model):
    DoesNotExist = None
    objects = None
    vendor = models.CharField(max_length=100)
    device = models.CharField(max_length=100)
