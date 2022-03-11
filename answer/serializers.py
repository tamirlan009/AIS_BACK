from rest_framework import serializers
from .models import Answer, AnswerImages


class AnswerImagesSerializer(serializers.ModelSerializer):
    """
    Сериалайзер таблицы AnswerImages
    """
    url = serializers.SerializerMethodField(method_name='get_url')

    class Meta:
        model = AnswerImages
        fields = '__all__'

    def get_url(self, obj):
        return obj.get_url()


class CreateAnswerSerializer(serializers.ModelSerializer):
    """
    Сериалайзер создания записи в таблицу Answer
    """
    answerimages = serializers.SerializerMethodField(method_name='get_images')
    replyDate = serializers.SerializerMethodField(method_name='convert_date')

    class Meta:
        model = Answer
        fields = '__all__'

    def get_images(self, obj):
        answerimages = obj.answerimages.all()

        serializer = AnswerImagesSerializer(answerimages, many=True)
        return serializer.data

    def convert_date(self, obj):
        return obj.replyDate.date()


class GetAnswerSerializer(serializers.ModelSerializer):
    answerimages = AnswerImagesSerializer(many=True)
    replyDate = serializers.SerializerMethodField(method_name='convert_date')

    class Meta:
        model = Answer
        fields = '__all__'

    def convert_date(self, obj):
        return obj.replyDate.date()
