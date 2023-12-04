from django.db import models
from django.utils import timezone

class Quote(models.Model):
    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'
        get_latest_by = 'created_at'

    text = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text