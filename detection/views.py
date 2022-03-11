import threading
from django.db.models import QuerySet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework import permissions
from ais.permissions import UserCanCreate, UserCanView
from .models import DetectedTable, Pothole
from .serializers import DetectedTableSerializer, DetectedTableSerializerWithPothole
from .tasks import run_detection


class RunDetection(CreateAPIView):
    """
    Запуск на детектирование
    """

    permission_classes = [permissions.IsAuthenticated, UserCanCreate]
    queryset = DetectedTable
    serializer_class = DetectedTableSerializer

    def perform_create(self, serializer):

        serializer.validated_data['creator'] = self.request.user
        table = serializer.save()
        run_detection.delay(table.id)

        #
        # detection = run_detection.PotholeDetection(
        #     'detection/model/yolov4-pothole.weights',
        #     'detection/model/yolov4-pothole.cfg',
        #     'detection/model/obj.names',
        #     416,
        #     table
        # )
        #
        # t = threading.Thread(target=detection.run)
        # t.start()


class DetectedList(ListAPIView):
    """
    Получение списка контрольных выездов
    """

    permission_classes = [permissions.IsAuthenticated, UserCanView]
    queryset = DetectedTable.objects.all()
    serializer_class = DetectedTableSerializer

    def get_queryset(self):

        assert self.queryset is not None, (
                "'%s' should either include a `queryset` attribute, "
                "or override the `get_queryset()` method."
                % self.__class__.__name__
        )

        if self.request.user.is_superuser:
            queryset = self.queryset.all()

        elif self.request.user.is_company_employee:
            queryset = self.queryset.filter(creator=self.request.user)

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()

        return queryset


class GetDetailDetection(RetrieveAPIView):
    """
    Получение контрольного выезда с изображениями
    """

    permission_classes = [permissions.IsAuthenticated, UserCanView]
    queryset = DetectedTable
    serializer_class = DetectedTableSerializerWithPothole


class DeleteDetection(DestroyAPIView):
    """
    Удалить контрольный везд
    """

    permission_classes = [permissions.IsAuthenticated, UserCanCreate]
    queryset = DetectedTable.objects.all()

    def perform_destroy(self, instance):
        if instance.creator == self.request.user or self.request.user.is_superuser:
            instance.delete()


class DeletePothole(DestroyAPIView):
    """
    Удалить изображение
    """

    permission_classes = [permissions.IsAuthenticated, UserCanCreate]
    queryset = Pothole.objects.all()

    def perform_destroy(self, instance):
        if instance.date_table_id.creator == self.request.user or self.request.user.is_superuser:
            instance.delete()













