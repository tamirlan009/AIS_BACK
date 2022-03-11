from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from .serializers import NotificationSerializer
from .models import NotificationTable


class NotificationConsumer(ListModelMixin, GenericAsyncAPIConsumer):

    queryset = NotificationTable.objects.all()
    serializer_class = NotificationSerializer



