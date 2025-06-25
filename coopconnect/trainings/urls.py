from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TrainingsViewSet
router=DefaultRouter()
router.register(r"trainings",TrainingsViewSet,
                basename="trainings")
urlpatterns = [
    path("", include(router.urls)),
]

