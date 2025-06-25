from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmerViewSet, VillageViewSet ,AdminViewSet

router = DefaultRouter()
router.register(r'farmer', FarmerViewSet, basename='farmer')
router.register(r'village', VillageViewSet, basename='village')
router.register(r'cooperativeadmin',AdminViewSet, basename='cooperative')

urlpatterns = [
    path('', include(router.urls)),
]