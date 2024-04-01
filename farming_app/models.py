from datetime import datetime
from django.db import models
from datetime import datetime

from django.dispatch import receiver
from datetime import date
from datetime import datetime
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.shortcuts import redirect
#from multiselectfield import MultiSelectField
from django.db import models
from django.contrib.auth.models import  AbstractBaseUser , BaseUserManager, PermissionsMixin
from django.db import models

class AccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    email= models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    username  = models.CharField(max_length=50, unique=True)
    phone_number= models.CharField(max_length=50)
    date_joined= models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = AccountManager()

    def _str_(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class Customer(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    profile_image = models.ImageField(upload_to='customer/%Y/%m/%d/', default='default.png')
    city = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    blood_group = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True)
    date_joined = models.DateTimeField(default=date.today, blank=True)
    date_of_birth = models.DateField(null=True)
    age_years = models.PositiveIntegerField(null=True)  

    @property
    def calculate_age(self):  
        today = date.today()
        if self.date_of_birth:
            age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
            return age
        return None
    
    def _str_(self):
        return f'{self.user.first_name} {self.user.last_name}'

class UserProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()



class Farm(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    soil_quality = models.CharField(max_length=50)
    pest_control = models.TextField()
    document = models.FileField(upload_to='farm_documents/', null=True, blank=True)

class Crop(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=100)
    crop_type = models.CharField(max_length=100)
    planting_date = models.DateTimeField()
    harvest_date = models.DateTimeField()
    document = models.FileField(upload_to='crop_documents/', null=True, blank=True)

class Harvest(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    harvest_date = models.DateField()
    yield_amount = models.FloatField()
    document = models.FileField(upload_to='harvest_documents/', null=True, blank=True)

class DailyUpdate(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    rainfall = models.FloatField()
    document = models.FileField(upload_to='daily_update_documents/', null=True, blank=True)

class WeatherData(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    rainfall = models.FloatField()
    document = models.FileField(upload_to='weather_data_documents/', null=True, blank=True)


class Fertilizer(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    description = models.TextField()
    nitrogen_content = models.FloatField()
    phosphorus_content = models.FloatField()
    potassium_content = models.FloatField()
    recommended_for_crop = models.ForeignKey('Crop', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Soil(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    description = models.TextField()
    texture = models.CharField(max_length=100, null=True, blank=True)
    pH_level = models.FloatField(null=True, blank=True)
    organic_matter = models.FloatField(null=True, blank=True)
    moisture_retention = models.FloatField(null=True, blank=True)
    drainage_capacity = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Group(models.Model):
    group_name = models.CharField(max_length=100)
    members_count = models.IntegerField()
    group_type = models.CharField(max_length=100)
    group_role = models.CharField(max_length=100)
    country_operation = models.CharField(max_length=100)

