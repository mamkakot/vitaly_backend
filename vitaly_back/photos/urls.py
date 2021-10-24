from django.urls import include, path
from rest_framework import routers
from .views import PhotoViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register(r'ratings', RatingViewSet)
router.register(r'photos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
