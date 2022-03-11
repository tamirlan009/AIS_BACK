from rest_framework import serializers
from .models import DetectedTable, Pothole


class PotholeSerializer(serializers.ModelSerializer):
    """
    Сериалайзер таблицы Pothole
    """

    class Meta:
        model = Pothole
        fields = '__all__'


class DetectedTableSerializer(serializers.ModelSerializer):
    """
    Сериалайзер таблицы DetectedTable
    """

    class Meta:
        model = DetectedTable
        fields = '__all__'


class DetectedTableSerializerWithPothole(serializers.ModelSerializer):
    """
    Сериалайзер таблицы DetectedTable с изображениями
    """
    pothols = PotholeSerializer(many=True)

    class Meta:
        model = DetectedTable
        fields = '__all__'
