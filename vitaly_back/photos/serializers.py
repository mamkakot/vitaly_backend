from rest_framework import serializers
from .models import Photo, Rating
from django.db.models import Avg


class RatingSerializer(serializers.ModelSerializer):
    photo = serializers.StringRelatedField()

    class Meta:
        model = Rating
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    # ratings = RatingSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = '__all__'

    def get_avg_rating(self, instance):
        return Rating.objects.filter(photo=instance).aggregate(Avg('value'))
