from django.urls import path
from . import views

urlpatterns = [
   
    # path('user/', views.UserView.as_view(), name='user_api'),
    # path('user_update/<int:pk>/', views.UserChangeView.as_view(), name='user_update'),

    path('farm/', views.FarmView.as_view(), name='farm_api'),
    path('farm_update/<int:pk>/', views.FarmChangeView.as_view(), name='farm_update'),

    path('crop/', views.CropView.as_view(), name='crop_api'),
    path('crop_update/<int:pk>/', views.CropChangeView.as_view(), name='crop_update'),

    path('harvest/', views.HarvestView.as_view(), name='harvest_api'),
    path('harvest_update/<int:pk>/', views.HarvestChangeView.as_view(), name='harvest_update'),

    path('weather_data/', views.WeatherDataView.as_view(), name='weather_data_api'),
    path('weather_data_update/<int:pk>/', views.WeatherDataChangeView.as_view(), name='weather_data_update'),

    path('soil/', views.SoilView.as_view(), name='soil_api'),
    path('soil_update/<int:pk>/', views.SoilChangeView.as_view(), name='soil_update'),

    path('fertilizer/', views.FertilizerView.as_view(), name='fertilizer_api'),
    path('fertilizer_update/<int:pk>/', views.FertilizerChangeView.as_view(), name='fertilizer_update'),
]
