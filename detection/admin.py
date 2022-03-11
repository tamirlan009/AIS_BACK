from django.contrib import admin
from .models import DetectedTable, Pothole, TrackerData

admin.site.register([DetectedTable, Pothole, TrackerData])