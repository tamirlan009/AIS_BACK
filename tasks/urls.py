from django.urls import path
from . import views

urlpatterns = [
    path('get/task/<int:pk>', views.GetCurrentsTask.as_view()),
    path('get/task/', views.GetAllCurrentTasks.as_view()),
    path('get/counttask/', views.GetCountTask.as_view()),
    path('get/category/', views.GetCategory.as_view()),
    path('post/create/task/', views.CreateTask.as_view()),
    path('put/update/task/<int:pk>', views.CloseTask.as_view()),
]
