
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dailyplanners, name="dailyplanners"),
    path('positivity', views.positivity, name="positivity"),
    path('dailyplanner/<int:plan_id>/', views.dailyplanner, name="dailyplanner")
]
