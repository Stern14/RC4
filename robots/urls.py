from django.urls import path
from . import views

urlpatterns = [
    path('api', views.api_robots, name='api_robots'),
    path('total-week', views.total_week, name = 'total-week'),
]