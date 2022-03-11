from rest_framework import serializers
from tasks.models import Task, Images
from tasks.serializers import CategorySerializer
from users.serializers import UserSerializer

class ImagesSerializer(serializers.ModelSerializer):
    """
    Сериалайзер таблицы Images
    """

    url = serializers.SerializerMethodField(method_name='get_url')

    class Meta:
        model = Images
        fields = ['id', 'url']

    def get_url(self, instance):
        return instance.get_url()


class GetTaskToMapSerialize(serializers.ModelSerializer):
    """
    Сериалайзер таблицы Task с выводом одного изображения таблицы Images
    """

    images = serializers.SerializerMethodField(method_name='get_image')
    category = CategorySerializer(many=False)
    executor = UserSerializer(many=False)
    creator = UserSerializer(many=False)
    state = serializers.SerializerMethodField(method_name='is_expired')
    createDate = serializers.SerializerMethodField(method_name='convert_date')


    class Meta:
        model = Task

        fields = ['id', 'images', 'category', 'executor', 'creator', 'state', 'createDate']

    def get_image(self, instance):
        queryset = instance.images.first()
        serializer = ImagesSerializer(queryset)

        return serializer.data

    def is_expired(self, obj):
        if not obj.is_done:
            if obj.expired:
                return 'просрочено'
            else:
                return 'на выполнении'
        else:
            return 'выполнено'

    def convert_date(self, obj):
        return obj.createDate.date()



