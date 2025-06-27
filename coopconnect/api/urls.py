from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import VillageViewSet

from .views import PaymentViewSet

router = DefaultRouter()

router.register(r"payment", PaymentViewSet, basename="payment")

urlpatterns = [path('', include(router.urls))]



router.register(r"village", VillageViewSet, basename="village")

urlpatterns = [path('', include(router.urls))]