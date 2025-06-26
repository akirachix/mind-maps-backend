# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import *

# router = DefaultRouter()
# router.register(r'users', FarmerViewSet,AdminViewSet,ExtensionWorkerViewSet, basename='users')

# urlpatterns = [
#     path('', include(router.urls)),
# ]from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import FarmerViewSet, AdminViewSet, ExtensionWorkerViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'users', ExtensionWorkerViewSet, basename='users')
router.register(r'cooperativeadmin', AdminViewSet, basename='admin')
router.register(r'extension', ExtensionWorkerViewSet, basename='extension')
router.register(r'farmer', FarmerViewSet, basename='farmer')

urlpatterns = [
    path('', include(router.urls)),
]