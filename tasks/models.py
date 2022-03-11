import pytz
from django.db import models
from datetime import datetime
from django.db.models import ExpressionWrapper, BooleanField, Q
from users.models import CustomUser


class ExpiredManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().annotate(
            expired=ExpressionWrapper(Q(leadTime__lt=datetime.now()), output_field=BooleanField())
        )


class Category(models.Model):
    name = models.CharField('название категории', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Таблица с категориями задач'
        verbose_name_plural = 'Таблица с категориями задач'


class Task(models.Model):
    category = models.ForeignKey(Category, verbose_name='категория задачи', null=True, blank=True,
                                 on_delete=models.SET_NULL,
                                 related_name='category')
    description = models.TextField(verbose_name='описание задачи', null=True)
    latitude = models.FloatField(verbose_name='широта местоположения', blank=True, null=True)
    longitude = models.FloatField(verbose_name='долгота местоположения', blank=True, null=True)
    address = models.TextField(verbose_name='адрес местоположения', blank=True, null=True)
    executor = models.ForeignKey(CustomUser, verbose_name='исполнитель', null=True, blank=True,
                                 on_delete=models.SET_NULL,
                                 related_name='executor')
    createDate = models.DateTimeField(verbose_name='дата создания и отправки на выполнение', auto_now_add=True)
    leadTime = models.DateTimeField(verbose_name='Срок выполнения', blank=True, null=True)
    is_done = models.BooleanField(verbose_name='задача выполнено или нет', default=False)
    creator = models.ForeignKey(CustomUser, verbose_name='создатель', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='creator')
    objects = ExpiredManager()

    def __str__(self):
        return self.category.name + ' ' + self.createDate.date().__str__()

    class Meta:
        ordering = ('-createDate',)
        verbose_name = 'Таблица с описанием задач'
        verbose_name_plural = 'Таблица с описанием задач'


class Images(models.Model):
    url = models.ImageField(upload_to='single_task/', blank=True, null=True)
    task = models.ForeignKey(Task, verbose_name='связанная задача', null=True, blank=True,
                             on_delete=models.CASCADE,
                             related_name='images')

    def get_url(self):
        return 'http://127.0.0.1:8000' + self.url.url

    def __str__(self):
        return self.url.url

    class Meta:
        verbose_name = 'Таблица с изображениями'
        verbose_name_plural = 'Таблица с изображениями'
