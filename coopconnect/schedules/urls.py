from django.urls import path
from . import views

urlpatterns = [
    path('', views.ScheduleListView.as_view(), name='schedule-list'),
]