from django.urls import path
from . import views

urlpatterns = [
    path('post/create/answer/', views.CreateAnswer.as_view()),
]

