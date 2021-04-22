from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    phone_number = models.TextField(null=True,blank=True)
    is_reader = models.BooleanField(default=True,null=False,blank=False)
    registration_timestamp = models.DateTimeField(auto_now_add=True)
    gender = models.BooleanField(null=False,blank=False)
    profile_image = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.first_name + self.last_name

class Story(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    episodes_count = models.IntegerField(blank=False,null=False)
    publishing_timestamp = models.DateTimeField(blank=True,null=True)
    likes_count = models.IntegerField(blank=True,null=True)
    views_count = models.IntegerField(blank=True,null=True)
    story_type = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    rate = models.FloatField(blank=True,null=True)

class Episode(models.Model):
    story_id = models.ForeignKey(Story,on_delete=models.CASCADE)
    episode_path = models.TextField(blank=False,null=False)
    upload_timestamp = models.DateTimeField(blank=True,null=True)
    likes_count = models.IntegerField(blank=True,null=True)
    views_count = models.IntegerField(blank=True,null=True)
    rate = models.FloatField(blank=True,null=True)

class Event(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField(blank=False,null=False)
    event_description = models.TextField(blank=True,null=True)
    starting_date = models.DateField(blank=True,null=True)
    ending_date = models.DateField(blank=True,null=True)

class EventParticipants(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event,on_delete=models.CASCADE)
    participating_timestamp = models.DateTimeField(null=True,blank=True)

class Contest(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField(blank=False,null=False)
    prize = models.TextField(blank=True,null=True)
    starting_timestamp = models.DateTimeField(null=True,blank=True)
    ending_timestamp = models.DateTimeField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)

class ContestParticipants(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    contest_id = models.ForeignKey(Contest,on_delete=models.CASCADE)
    participating_timestamp = models.DateTimeField(null=True,blank=True)

class Comments(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    story_id = models.ForeignKey(Story,on_delete=models.CASCADE)
    comment_timezone = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    comment_text = models.TextField(blank=False,null=False)
    likes_count = models.IntegerField(blank=True,null=True)









