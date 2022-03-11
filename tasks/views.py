from datetime import datetime, timedelta
from django.db.models import QuerySet, Q
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView,UpdateAPIView
from ais.permissions import UserHasAccess, UserCanCreate
from .serializers import TaskSerializer, AllTasksSerializer, CreateTaskSerializer, \
    GetCategorySerializer, UpdateTaskSerializer
from .models import Task, Images, Category


class SetPagination(pagination.PageNumberPagination):
    """
    Настройки пагинации
    """

    page_size = 10
    page_size_query_param = 'page_size'
    ordering = 'created_at'


class GetCurrentsTask(RetrieveAPIView):
    """
    Получить текущую задачу
    """

    permission_classes = [permissions.IsAuthenticated, UserHasAccess]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class GetAllCurrentTasks(ListAPIView):
    """
    Получить все задачи
    """

    permission_classes = [permissions.IsAuthenticated]
    pagination_class = SetPagination
    queryset = Task.objects.all()
    serializer_class = AllTasksSerializer

    def get_model_with_condition(self):
        param = self.request.query_params.get('value')

        if param:
            if param == 'all_tasks':
                return self.queryset.filter(Q(expired=False) & Q(is_done=False))

            elif param == 'new_tasks':
                return self.queryset.filter(Q(expired=False) & Q(createDate__gte=datetime.today()-timedelta(days=2))
                                            & Q(is_done=False))

            elif param == 'expiring_tasks':
                return self.queryset.filter(Q(expired=False) & Q(leadTime__lte=datetime.today()-timedelta(days=14)) &
                                            Q(is_done=False) & Q(expired=False))

            elif param == 'expired_tasks':
                return self.queryset.filter(Q(expired=True) & Q(is_done=False))

            elif param == 'is_done':
                return self.queryset.filter(is_done=True)

            elif param == 'all':
                return self.queryset.all()

        return self.queryset.all()

    def get_queryset(self):

        assert self.queryset is not None, (
                "'%s' should either include a `queryset` attribute, "
                "or override the `get_queryset()` method."
                % self.__class__.__name__
        )

        if self.request.user.is_superuser:
            queryset = self.get_model_with_condition()

        elif self.request.user.is_company_employee:
            self.queryset = self.queryset.filter(creator=self.request.user)
            queryset = self.get_model_with_condition()

        elif self.request.user.is_contractor:
            self.queryset = self.queryset.filter(executor=self.request.user)
            queryset = self.get_model_with_condition()

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()

        return queryset


class CreateTask(CreateAPIView):
    """
    Создать задачу
    """

    permission_classes = [permissions.IsAuthenticated, UserCanCreate]
    queryset = Task
    serializer_class = CreateTaskSerializer

    def perform_create(self, serializer):
        serializer.validated_data['creator'] = self.request.user
        task = serializer.save()

        images = self.request.FILES.getlist('images')

        for image in images:
            Images.objects.create(
                url=image,
                task=task
            )


class GetCountTask(APIView):
    """
    Получить статистику по текущим задачам
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if self.request.user.is_superuser:
            queryset = Task.objects.all()

        else:
            queryset = Task.objects.filter(Q(creator=self.request.user) | Q(executor=self.request.user))

        count_all_tasks = queryset.filter(Q(is_done=False) & Q(expired=False)).count()
        count_new_tasks = queryset.filter(Q(createDate__gte=datetime.today()-timedelta(days=2)) & Q(is_done=False)
                                          & Q(expired=False)).count()
        count_expiring_tasks = queryset.filter(Q(leadTime__lte=datetime.today()-timedelta(days=14)) & Q(is_done=False) &
                                               Q(expired=False)).count()

        data = {
            'count_all_tasks': count_all_tasks,
            'count_new_tasks': count_new_tasks,
            'count_expiring_tasks': count_expiring_tasks,
        }

        return Response(data)


class GetCategory(ListAPIView):
    """
    Получить категории задач
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = GetCategorySerializer


class CloseTask(UpdateAPIView):
    """
    Закрыть задачу
    """

    permission_classes = [permissions.IsAuthenticated, UserCanCreate]
    queryset = Task.objects.all()
    serializer_class = UpdateTaskSerializer








