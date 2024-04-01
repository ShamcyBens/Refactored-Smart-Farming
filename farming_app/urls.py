from django.urls import path
from farming_app import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('register/',views.farmerregister, name='register'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('farm/',farm_form_view, name='farm_form'),
    path('crop/',crop_form_view, name='crop_form'),
    path('harvest/',harvest_form_view, name='harvest_form'),
    path('daily_update/',daily_update_form_view, name='daily_update_form'),
    path('weather_data/',weather_data_form_view, name='weather_data_form'),
    path('fertilizer/',fertilizer_form_view, name='fertilizer_form'),
    path('soil/',soil_form_view, name='soil_form'),
    path('proceed/',views.proceed, name='proceed'),
    path('create_group/',views.create_group, name='create_group'),
    path('join_group/', views.join_group, name='join_group'),
    path('specific_join_group/', views.specific_join_group, name='specific_join_group'),

]


