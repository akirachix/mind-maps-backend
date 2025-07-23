from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import (
    TrainingsViewSet,
    SchedulesViewSet,
    RewardsViewSet,
    VillageViewSet,
    UserViewSet,
    RefundViewSet,
    AttendanceViewSet,
    PaymentViewSet,
    daraja_callback,
    STKPushView,
)

router = DefaultRouter()
router.register(r"trainings", TrainingsViewSet, basename="trainings")
router.register(r"schedules", SchedulesViewSet, basename="schedules")
router.register(r"rewards", RewardsViewSet, basename="rewards")
router.register(r"village", VillageViewSet, basename="village")
router.register(r'users', UserViewSet, basename='user') 
router.register(r'refunds', RefundViewSet, basename='refund')
router.register(r'attendance', AttendanceViewSet, basename='attendance')
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [
    path("", include(router.urls)),
    path('daraja/stk-push/', STKPushView.as_view(), name='daraja-stk-push'),
    path('daraja/callback/', daraja_callback, name='daraja-callback'),
]
