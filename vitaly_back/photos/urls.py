from django.urls import include, path
from rest_framework import routers
from .views import PhotoViewSet, RatingViewSet, UserIpViewSet

router = routers.DefaultRouter()
router.register(r'ratings', RatingViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'user_ips', UserIpViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
