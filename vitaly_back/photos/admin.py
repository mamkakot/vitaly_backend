from django.contrib import admin
from .models import Photo, Rating, UserIp

admin.site.register(Photo)
admin.site.register(Rating)
admin.site.register(UserIp)
