from django.db import models
from apps.accounts.models import User
from apps.stories.models import Story
# Create your models here.

"""
Comments Model:
this model is used to save comment's data
"""
class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
    comment_timezone = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    comment_text = models.TextField(blank=False, null=False)
    likes_count = models.IntegerField(blank=True, null=True)