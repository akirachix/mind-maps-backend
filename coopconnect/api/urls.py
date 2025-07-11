from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import RewardsViewSet
from .views import SchedulesViewSet
from .views import TrainingsViewSet
from .views import VillageViewSet

router=DefaultRouter()
router.register(r"rewards",RewardsViewSet,
                basename="rewards")
router.register(r"schedules",SchedulesViewSet,
                basename="schedules")
router.register(r"trainings",TrainingsViewSet,
                basename="trainings")
router.register(r"village",VillageViewSet,
                basename="village")
urlpatterns = [
   path("", include(router.urls)),
]




