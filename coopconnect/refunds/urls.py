from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RefundViewSet

router=DefaultRouter()
router.register(r"",RefundViewSet, basename='refund')

urlpatterns=[
    path('',include(router.urls)),
]