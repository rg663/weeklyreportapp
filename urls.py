from django.urls import path

from . import views

app_name = "weeklyreportapp"
urlpatterns = [
    path("weeklyreportpage/", views.index),
]
