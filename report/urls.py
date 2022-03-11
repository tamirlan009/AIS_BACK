from django.urls import path
from . import views

urlpatterns = [
    path('get/counttaskreport', views.CountTaskReport.as_view()),
]
