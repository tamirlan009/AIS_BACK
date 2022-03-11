from django.urls import path
from . import views

urlpatterns = [
    path('post/rundetection', views.RunDetection.as_view()),
    path('get/detection/list', views.DetectedList.as_view()),
    path('get/detection/<int:pk>', views.GetDetailDetection.as_view()),
    path('delete/detection/<int:pk>', views.DeleteDetection.as_view()),
    path('delete/pothole/<int:pk>', views.DeletePothole.as_view()),
]
