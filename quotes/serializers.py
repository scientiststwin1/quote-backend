from . import models
from rest_framework import serializers

class QuoteSerializer(serializers.ModelSerializer):
 class Meta:
  model = models.Quote
  fields = ['id', 'text', 'author', 'created_at', 'updated_at']
  read_only_fields = ('id', 'created_at', 'updated_at')