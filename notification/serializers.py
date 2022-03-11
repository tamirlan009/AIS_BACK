from rest_framework import serializers
from .models import NotificationTable


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = NotificationTable
        fields = '__all__'


