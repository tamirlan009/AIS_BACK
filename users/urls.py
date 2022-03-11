from django.urls import path
from .views import GetCurrentUser, GetRelatedUser, MyTokenObtainPairView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token'),
    # # path('api/v1/refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('get/user', GetCurrentUser.as_view()),
    path('get/related_user', GetRelatedUser.as_view()),
]
