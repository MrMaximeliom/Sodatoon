from django.db import models
from apps.stories.models import Story

"""
Episode Model:
this model is used to save episode's data
"""
class Episode(models.Model):
    story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
    episode_path = models.TextField(blank=False, null=False)
    upload_timestamp = models.DateTimeField(blank=True, null=True)
    likes_count = models.IntegerField(blank=True, null=True)
    views_count = models.IntegerField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)

    class Meta:
        db_table='episode'