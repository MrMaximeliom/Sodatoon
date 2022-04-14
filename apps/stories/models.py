from django.db import models
from apps.accounts.models import User

"""
Story Model:
this model is used to save story's data
"""
class Story(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    episodes_count = models.IntegerField(blank=False, null=False)
    publishing_timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    likes_count = models.IntegerField(blank=True, null=True)
    views_count = models.IntegerField(blank=True, null=True)
    story_type = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    story_name = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.story_name
    class Meta:
        db_table = "story"