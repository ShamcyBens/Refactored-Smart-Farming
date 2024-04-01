from .models import *
from django.forms import DateInput
from django.forms.fields import DateField
from django.forms.widgets import PasswordInput
from django import forms
from django.forms import DateInput, DateField, PasswordInput
from .models import UserProfile, Farm, Crop, Harvest, DailyUpdate, WeatherData,Soil, Fertilizer

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput(attrs={
        
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password', ]
    
    def _init_(self, *args, **kwargs):
        super(RegistrationForm, self)._init_(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
    

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['profile_image', 'city', 'address', 'country', 'date_of_birth', 'gender']

    def _init_(self, *args, **kwargs):
        super(CustomerForm, self)._init_(*args, **kwargs)
        self.fields['profile_image'].widget.attrs['class'] = 'upload'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'
        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address',]


class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = '__all__'


class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = '__all__'


class HarvestForm(forms.ModelForm):
    class Meta:
        model = Harvest
        fields = '__all__'


class DailyUpdateForm(forms.ModelForm):
    class Meta:
        model = DailyUpdate
        fields = '__all__'

class WeatherDataForm(forms.ModelForm):
    class Meta:
        model = WeatherData
        fields = '__all__'


class SoilForm(forms.ModelForm):
    class Meta:
        model = Soil
        fields = '__all__'


class FertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer
        fields = '__all__'
        
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
