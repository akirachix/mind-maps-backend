from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import RewardsViewSet
from .views import SchedulesViewSet
from .views import TrainingsViewSet
router=DefaultRouter()
router.register(r"rewards",RewardsViewSet,
                basename="rewards")
router.register(r"schedules",SchedulesViewSet,
                basename="schedules")
router.register(r"trainings",TrainingsViewSet,
                basename="trainings")
urlpatterns = [
   path("", include(router.urls)),
]




