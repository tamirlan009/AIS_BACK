from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('tasks.urls')),
    path('api/v1/', include('answer.urls')),
    path('api/v1/', include('detection.urls')),
    path('api/v1/', include('map.urls')),
    path('api/v1/', include('report.urls')),
    path('index/', include('notification.urls')),
    path('api/v1/refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
