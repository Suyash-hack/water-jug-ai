from django.urls import path
from .views import water_jug_solver

urlpatterns = [
    path('water-jug/', water_jug_solver),
]
