from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from farming_app.models import Account, Crop, DailyUpdate, Farm, Fertilizer, Harvest, Soil, WeatherData
from smart_farming import *
from .serializers import AccountSerializer, FarmSerializer, CropSerializer, HarvestSerializer, DailyUpdateSerializer, WeatherDataSerializer, SoilSerializer, FertilizerSerializer

class AccountView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AccountSerializer

    @swagger_auto_schema(responses={200: AccountSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=AccountSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AccountSerializer

    @swagger_auto_schema(responses={200: AccountSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        account = get_object_or_404(Account, pk=pk)
        serializer = AccountSerializer(account)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AccountSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        account = get_object_or_404(Account, pk=pk)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        account = get_object_or_404(Account, pk=pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FarmView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = FarmSerializer

    @swagger_auto_schema(responses={200: FarmSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        farms = Farm.objects.all()
        serializer = FarmSerializer(farms, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=FarmSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = FarmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FarmChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = FarmSerializer

    @swagger_auto_schema(responses={200: FarmSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        farm = get_object_or_404(Farm, pk=pk)
        serializer = FarmSerializer(farm)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=FarmSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        farm = get_object_or_404(Farm, pk=pk)
        serializer = FarmSerializer(farm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        farm = get_object_or_404(Farm, pk=pk)
        farm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CropView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CropSerializer

    @swagger_auto_schema(responses={200: CropSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        crops = Crop.objects.all()
        serializer = CropSerializer(crops, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CropSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = CropSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CropChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CropSerializer

    @swagger_auto_schema(responses={200: CropSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        crop = get_object_or_404(Crop, pk=pk)
        serializer = CropSerializer(crop)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CropSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        crop = get_object_or_404(Crop, pk=pk)
        serializer = CropSerializer(crop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        crop = get_object_or_404(Crop, pk=pk)
        crop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HarvestView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = HarvestSerializer

    @swagger_auto_schema(responses={200: HarvestSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        harvests = Harvest.objects.all()
        serializer = HarvestSerializer(harvests, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=HarvestSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = HarvestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HarvestChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = HarvestSerializer

    @swagger_auto_schema(responses={200: HarvestSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        harvest = get_object_or_404(Harvest, pk=pk)
        serializer = HarvestSerializer(harvest)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=HarvestSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        harvest = get_object_or_404(Harvest, pk=pk)
        serializer = HarvestSerializer(harvest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        harvest = get_object_or_404(Harvest, pk=pk)
        harvest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DailyUpdateView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DailyUpdateSerializer

    @swagger_auto_schema(responses={200: DailyUpdateSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        daily_updates = DailyUpdate.objects.all()
        serializer = DailyUpdateSerializer(daily_updates, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=DailyUpdateSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = DailyUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DailyUpdateChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DailyUpdateSerializer

    @swagger_auto_schema(responses={200: DailyUpdateSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        daily_update = get_object_or_404(DailyUpdate, pk=pk)
        serializer = DailyUpdateSerializer(daily_update)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=DailyUpdateSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        daily_update = get_object_or_404(DailyUpdate, pk=pk)
        serializer = DailyUpdateSerializer(daily_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        daily_update = get_object_or_404(DailyUpdate, pk=pk)
        daily_update.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WeatherDataView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = WeatherDataSerializer

    @swagger_auto_schema(responses={200: WeatherDataSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        weather_data = WeatherData.objects.all()
        serializer = WeatherDataSerializer(weather_data, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=WeatherDataSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = WeatherDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WeatherDataView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = WeatherDataSerializer

    @swagger_auto_schema(responses={200: WeatherDataSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        weather_data = WeatherData.objects.all()
        serializer = WeatherDataSerializer(weather_data, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=WeatherDataSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = WeatherDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WeatherDataChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = WeatherDataSerializer

    @swagger_auto_schema(responses={200: WeatherDataSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        weather_data = get_object_or_404(WeatherData, pk=pk)
        serializer = WeatherDataSerializer(weather_data)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=WeatherDataSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        weather_data = get_object_or_404(WeatherData, pk=pk)
        serializer = WeatherDataSerializer(weather_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        weather_data = get_object_or_404(WeatherData, pk=pk)
        weather_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SoilView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SoilSerializer

    @swagger_auto_schema(responses={200: SoilSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        soil_data = Soil.objects.all()
        serializer = SoilSerializer(soil_data, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=SoilSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = SoilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SoilChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SoilSerializer

    @swagger_auto_schema(responses={200: SoilSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        soil_data = get_object_or_404(Soil, pk=pk)
        serializer = SoilSerializer(soil_data)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SoilSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        soil_data = get_object_or_404(Soil, pk=pk)
        serializer = SoilSerializer(soil_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        soil_data = get_object_or_404(Soil, pk=pk)
        soil_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FertilizerView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = FertilizerSerializer

    @swagger_auto_schema(responses={200: FertilizerSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        fertilizers = Fertilizer.objects.all()
        serializer = FertilizerSerializer(fertilizers, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=FertilizerSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = FertilizerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FertilizerChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = FertilizerSerializer

    @swagger_auto_schema(responses={200: FertilizerSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        fertilizer = get_object_or_404(Fertilizer, pk=pk)
        serializer = FertilizerSerializer(fertilizer)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=FertilizerSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        fertilizer = get_object_or_404(Fertilizer, pk=pk)
        serializer = FertilizerSerializer(fertilizer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        fertilizer = get_object_or_404(Fertilizer, pk=pk)
        fertilizer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
       
