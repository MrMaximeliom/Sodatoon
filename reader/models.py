from django.db import models

from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserAccountManager(BaseUserManager):

    def create_user(self, email, username, first_name, last_name, gender, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not first_name:
            raise ValueError('Users must provide their first name')
        if not last_name:
            raise ValueError('Users must provide their last name')
        if not gender:
            raise ValueError('Users must provide their gender')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            gender=gender,


        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, gender,
                         password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,

            first_name=first_name,
            last_name=last_name,
            gender=gender,
            password = password

        )
        #user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    from utils.constants import COUNTRIES, GENDER_CHOICES
    alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabet characters are allowed.')
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_artist = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    # ,help_text = 'Only alphabet characters are allowed.'
    first_name = models.CharField(verbose_name='first name', max_length=40,validators=[alphanumeric])
    last_name = models.CharField(verbose_name='last name', max_length=40,validators=[alphanumeric])
    gender = models.CharField(verbose_name='gender', choices=GENDER_CHOICES, max_length=10)
    # password = models.CharField(verbose_name='password', max_length=128)
    profile_pic = models.CharField(verbose_name='profile picture', max_length=320,blank=True)
    country = models.CharField(verbose_name='country', choices=COUNTRIES, max_length=180,blank=True,null=True)
    USERNAME_FIELD = 'email'
    # 'username', 'first_name', 'last_name', 'gender'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name','gender']
    objects = UserAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_level):
        return True
# class User(AbstractUser):
#     date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     phone_number = models.TextField(null=True,blank=True)
#     is_reader = models.BooleanField(default=True,null=False,blank=False)
#     registration_timestamp = models.DateTimeField(auto_now_add=True)
#     gender = models.CharField(null=False,blank=False, choices=GENDER_CHOICES,
#         default=MALE,max_length=7)
#     profile_image = models.TextField(null=True,blank=True)
#     def __str__(self):
#         return self.first_name + self.last_name

class Story(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    episodes_count = models.IntegerField(blank=False,null=False)
    publishing_timestamp = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    likes_count = models.IntegerField(blank=True,null=True)
    views_count = models.IntegerField(blank=True,null=True)
    story_type = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    rate = models.FloatField(blank=True,null=True)
    story_name = models.TextField(blank=False,null=False)

    def __str__(self):
        return self.story_name

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

    def __str__(self):
        return self.title

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

    def __str__(self):
        return self.title

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









