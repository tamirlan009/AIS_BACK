from rest_framework import serializers
from .models import Task, Category, Images
from users.models import CustomUser
from answer.serializers import GetAnswerSerializer


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериалайзер таблицы Category
    """

    class Meta:
        model = Category
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    """
    Сериалайзер таблицы CustomUser
    """

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'number_phone']


class ImagesSerializer(serializers.ModelSerializer):
    """
    Сериалайзер таблицы Images
    """

    class Meta:
        model = Images
        fields = ['id', 'url']


class TaskSerializer(serializers.ModelSerializer):
    """
    Сериалайзер таблицы Task
    """

    category = CategorySerializer(many=False)
    executor = UserSerializer(many=False)
    creator = UserSerializer(many=False)
    images = ImagesSerializer(many=True)
    answer = GetAnswerSerializer(many=True)
    state = serializers.SerializerMethodField(method_name='is_expired')
    createDate = serializers.SerializerMethodField(method_name='convert_date')

    class Meta:
        model = Task
        fields = '__all__'

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


class AllTasksSerializer(serializers.ModelSerializer):
    """
    Сериалайзер таблицы Task
    """

    category = CategorySerializer(many=False)
    executor = UserSerializer(many=False)
    createDate = serializers.SerializerMethodField(method_name='convert_date')
    state = serializers.SerializerMethodField(method_name='is_expired')
    creator = UserSerializer(many=False)

    class Meta:
        model = Task
        fields = 'id', 'description', 'category', 'description', 'createDate', 'creator', 'executor', 'state'

    def convert_date(self, obj):
        return obj.createDate.date()

    def is_expired(self, obj):
        if not obj.is_done:
            if obj.expired:
                return 'просрочено'
            else:
                return 'на выполнении'
        else:
            return 'выполнено'


class UpdateTaskSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для закрытия задачи
    """

    class Meta:
        model = Task
        fields = ['is_done']




class CreateImagesSerializer(serializers.ModelSerializer):
    """
    Сериалайзер таблицы Images
    """

    class Meta:
        model = Images
        fields = '__all__'


class CreateTaskSerializer(serializers.ModelSerializer):
    """
    Сериалайзер записи в таблицу Task
    """

    class Meta:
        model = Task
        fields = '__all__'


class GetCategorySerializer(serializers.ModelSerializer):
    """
    Сериалайзер таблицы Category
    """

    class Meta:
        model = Category
        fields = '__all__'
