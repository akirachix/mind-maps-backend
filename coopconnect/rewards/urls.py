from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import RewardsViewSet
router=DefaultRouter()
router.register(r"rewards",RewardsViewSet,
                basename="rewards")
urlpatterns = [
   path("", include(router.urls)),
]
