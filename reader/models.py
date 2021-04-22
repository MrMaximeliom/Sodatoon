from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser,AbstractBaseUser, BaseUserManager

# Create your models here.
FEMALE = 'Female'
MALE = 'Male'
GENDER_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
]
COUNTRIES = (
    ('Afghanistan', 'Afghanistan'),
    ('Albania', 'Albania'),
    ('Andorra', 'Andorra'),
    ('Angola', 'Angola'),
    ('Antigua & Deps', 'Antigua & Deps'),
    ('Argentina', 'Argentina'),
    ('Armenia', 'Armenia'),
    ('Australia', 'Australia'),
    ('Austria', 'Austria'),
    ('Azerbaijan', 'Azerbaijan'),
    ('Bahamas', 'Bahamas'),
    ('Bahrain', 'Bahrain'),
    ('Bangladesh', 'Bangladesh'),
    ('Barbados', 'Barbados'),
    ('Belarus', 'Belarus'),
    ('Belgium', 'Belgium'),
    ('Belize', 'Belize'),
    ('Benin', 'Benin'),
    ('Bhutan', 'Bhutan'),
    ('Bolivia', 'Bolivia'),
    ('Bosnia Herzegovina', 'Bosnia Herzegovina'),
    ('Botswana', 'Botswana'),
    ('Brazil', 'Brazil'),
    ('Brunei', 'Brunei'),
    ('Bulgaria', 'Bulgaria'),
    ('Burkina', 'Burkina'),
    ('Burundi', 'Burundi'),
    ('Cambodia', 'Cambodia'),
    ('Cameroon', 'Cameroon'),
    ('Canada', 'Canada'),
    ('Cape Verde', 'Cape Verde'),
    ('Central African Rep', 'Central African Rep'),
    ('Chad', 'Chad'),
    ('Chile', 'Chile'),
    ('China', 'China'),
    ('Colombia', 'Colombia'),
    ('Comoros', 'Comoros'),
    ('Congo', 'Congo'),
    ('Congo {Democratic Rep}', 'Congo {Democratic Rep}'),
    ('Costa Rica', 'Costa Rica'),
    ('Croatia', 'Croatia'),
    ('Cuba', 'Cuba'),
    ('Cyprus', 'Cyprus'),
    ('Czech Republic', 'Czech Republic'),
    ('Denmark', 'Denmark'),
    ('Djibouti', 'Djibouti'),
    ('Dominica', 'Dominica'),
    ('Dominican Republic', 'Dominican Republic'),
    ('East Timor', 'East Timor'),
    ('Ecuador', 'Ecuador'),
    ('Egypt', 'Egypt'),
    ('El Salvador', 'El Salvador'),
    ('Equatorial Guinea', 'Equatorial Guinea'),
    ('Eritrea', 'Eritrea'),
    ('Estonia', 'Estonia'),
    ('Ethiopia', 'Ethiopia'),
    ('Fiji', 'Fiji'),
    ('Finland', 'Finland'),
    ('France', 'France'),
    ('Gabon', 'Gabon'),
    ('Gambia', 'Gambia'),
    ('Georgia', 'Georgia'),
    ('Germany', 'Germany'),
    ('Ghana', 'Ghana'),
    ('Greece', 'Greece'),
    ('Grenada', 'Grenada'),
    ('Guatemala', 'Guatemala'),
    ('Guinea', 'Guinea'),
    ('Guinea-Bissau', 'Guinea-Bissau'),
    ('Guyana', 'Guyana'),
    ('Haiti', 'Haiti'),
    ('Honduras', 'Honduras'),
    ('Hungary', 'Hungary'),
    ('Iceland', 'Iceland'),
    ('India', 'India'),
    ('Indonesia', 'Indonesia'),
    ('Iran', 'Iran'),
    ('Iraq', 'Iraq'),
    ('Ireland {Republic}', 'Ireland {Republic}'),
    ('Israel', 'Israel'),
    ('Italy', 'Italy'),
    ('Ivory Coast', 'Ivory Coast'),
    ('Jamaica', 'Jamaica'),
    ('Japan', 'Japan'),
    ('Jordan', 'Jordan'),
    ('Kazakhstan', 'Kazakhstan'),
    ('Kenya', 'Kenya'),
    ('Kiribati', 'Kiribati'),
    ('Korea North', 'Korea North'),
    ('Korea South', 'Korea South'),
    ('Kosovo', 'Kosovo'),
    ('Kuwait', 'Kuwait'),
    ('Kyrgyzstan', 'Kyrgyzstan'),
    ('Laos', 'Laos'),
    ('Latvia', 'Latvia'),
    ('Lebanon', 'Lebanon'),
    ('Lesotho', 'Lesotho'),
    ('Liberia', 'Liberia'),
    ('Libya', 'Libya'),
    ('Liechtenstein', 'Liechtenstein'),
    ('Lithuania', 'Lithuania'),
    ('Luxembourg', 'Luxembourg'),
    ('Macedonia', 'Macedonia'),
    ('Madagascar', 'Madagascar'),
    ('Malawi', 'Malawi'),
    ('Malaysia', 'Malaysia'),
    ('Maldives', 'Maldives'),
    ('Mali', 'Mali'),
    ('Malta', 'Malta'),
    ('Marshall Islands', 'Marshall Islands'),
    ('Mauritania', 'Mauritania'),
    ('Mauritius', 'Mauritius'),
    ('Mexico', 'Mexico'),
    ('Micronesia', 'Micronesia'),
    ('Moldova', 'Moldova'),
    ('Monaco', 'Monaco'),
    ('Mongolia', 'Mongolia'),
    ('Montenegro', 'Montenegro'),
    ('Morocco', 'Morocco'),
    ('Mozambique', 'Mozambique'),
    ('Myanmar, {Burma}', 'Myanmar, {Burma}'),
    ('Namibia', 'Namibia'),
    ('Nauru', 'Nauru'),
    ('Nepal', 'Nepal'),
    ('Netherlands', 'Netherlands'),
    ('New Zealand', 'New Zealand'),
    ('Nicaragua', 'Nicaragua'),
    ('Niger', 'Niger'),
    ('Nigeria', 'Nigeria'),
    ('Norway', 'Norway'),
    ('Oman', 'Oman'),
    ('Pakistan', 'Pakistan'),
    ('Palau', 'Palau'),
    ('Panama', 'Panama'),
    ('Papua New Guinea', 'Papua New Guinea'),
    ('Paraguay', 'Paraguay'),
    ('Peru', 'Peru'),
    ('Philippines', 'Philippines'),
    ('Poland', 'Poland'),
    ('Portugal', 'Portugal'),
    ('Qatar', 'Qatar'),
    ('Romania', 'Romania'),
    ('Russian Federation', 'Russian Federation'),
    ('Rwanda', 'Rwanda'),
    ('St Kitts & Nevis', 'St Kitts & Nevis'),
    ('St Lucia', 'St Lucia'),
    ('Saint Vincent & the Grenadines', 'Saint Vincent & the Grenadines'),
    ('Samoa', 'Samoa'),
    ('San Marino', 'San Marino'),
    ('Sao Tome & Principe', 'Sao Tome & Principe'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Senegal', 'Senegal'),
    ('Serbia', 'Serbia'),
    ('Seychelles', 'Seychelles'),
    ('Sierra Leone', 'Sierra Leone'),
    ('Singapore', 'Singapore'),
    ('Slovakia', 'Slovakia'),
    ('Slovenia', 'Slovenia'),
    ('Solomon Islands', 'Solomon Islands'),
    ('Somalia', 'Somalia'),
    ('South Africa', 'South Africa'),
    ('South Sudan', 'South Sudan'),
    ('Spain', 'Spain'),
    ('Sri Lanka', 'Sri Lanka'),
    ('Sudan', 'Sudan'),
    ('Suriname', 'Suriname'),
    ('Swaziland', 'Swaziland'),
    ('Sweden', 'Sweden'),
    ('Switzerland', 'Switzerland'),
    ('Syria', 'Syria'),
    ('Taiwan', 'Taiwan'),
    ('Tajikistan', 'Tajikistan'),
    ('Tanzania', 'Tanzania'),
    ('Thailand', 'Thailand'),
    ('Togo', 'Togo'),
    ('Tonga', 'Tonga'),
    ('Trinidad & Tobago', 'Trinidad & Tobago'),
    ('Tunisia', 'Tunisia'),
    ('Turkey', 'Turkey'),
    ('Turkmenistan', 'Turkmenistan'),
    ('Tuvalu', 'Tuvalu'),
    ('Uganda', 'Uganda'),
    ('Ukraine', 'Ukraine'),
    ('United Arab Emirates', 'United Arab Emirates'),
    ('United Kingdom', 'United Kingdom'),
    ('United States', 'United States'),
    ('Uruguay', 'Uruguay'),
    ('Uzbekistan', 'Uzbekistan'),
    ('Vanuatu', 'Vanuatu'),
    ('Vatican City', 'Vatican City'),
    ('Venezuela', 'Venezuela'),
    ('Vietnam', 'Vietnam'),
    ('Yemen', 'Yemen'),
    ('Zambia', 'Zambia'),
    ('Zimbabwe', 'Zimbabwe')
)

"""
الكلاس المسؤول عن معالجة أخطاء الادخال بالنسبة لمعلومات تسجيل الطالب والمعلم
"""
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

"""
الجدول الأساسي للمستخدم في دجانجو تم إعادة تعريف حقوله وإضافة المزيد من الحقول 
والتي تعتبر مهمة بالنسبة للنظام
"""
class User(AbstractBaseUser):
    alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabet characters are allowed.')
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_reader = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    # ,help_text = 'Only alphabet characters are allowed.'
    first_name = models.CharField(verbose_name='first name', max_length=40,validators=[alphanumeric])
    last_name = models.CharField(verbose_name='last name', max_length=40,validators=[alphanumeric])
    gender = models.CharField(verbose_name='gender', choices=GENDER_CHOICES, max_length=10)
    # password = models.CharField(verbose_name='password', max_length=128)
    profile_pic = models.CharField(verbose_name='profile picture', max_length=320,blank=True)
    country = models.CharField(verbose_name='country', choices=COUNTRIES, max_length=180,blank=True)
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









