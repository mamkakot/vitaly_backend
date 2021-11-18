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
    lookup_field = 'ip'
    lookup_value_regex = '[0-9.]+'
    queryset = UserIp.objects.all()
    serializer_class = UserIpSerializer
