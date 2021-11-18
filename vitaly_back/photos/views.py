from django.shortcuts import render

from rest_framework import viewsets
from .models import Photo, Rating, UserIp
from .serializers import PhotoSerializer, RatingSerializer, UserIpSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class UserIpViewSet(viewsets.ModelViewSet):
    queryset = UserIp.objects.all()
    serializer_class = UserIpSerializer
