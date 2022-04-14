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
            password=password

        )
        # user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


"""
User Model:
this model is used to save users' data
"""


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
    first_name = models.CharField(verbose_name='first name', max_length=40, validators=[alphanumeric])
    last_name = models.CharField(verbose_name='last name', max_length=40, validators=[alphanumeric])
    gender = models.CharField(verbose_name='gender', choices=GENDER_CHOICES, max_length=10)
    # password = models.CharField(verbose_name='password', max_length=128)
    profile_pic = models.CharField(verbose_name='profile picture', max_length=320, blank=True)
    country = models.CharField(verbose_name='country', choices=COUNTRIES, max_length=180, blank=True, null=True)
    USERNAME_FIELD = 'email'
    # 'username', 'first_name', 'last_name', 'gender'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'gender']
    objects = UserAccountManager()

    def __str__(self):
        # objects of this model will be referenced by their usernames'
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_level):
        return True

    class Meta:
        # this is the actual table's name in the database
        db_table = 'user'



















