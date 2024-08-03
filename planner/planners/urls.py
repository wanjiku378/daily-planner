

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dailyplanners, name="dailyplanners"),
    path('add_plan', views.add_plan, name="add_plan"),
    path('dailyplanner<int:plan_id>/', views.dailyplanner, name="dailyplanner"),
]