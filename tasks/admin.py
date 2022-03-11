from django.contrib import admin
from .models import Task, Images, Category

admin.site.register([Task, Images, Category])

