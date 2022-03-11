from django.db import models
from users.models import CustomUser


class DetectedTable(models.Model):
    """
    Таблица с данными о каждом выезде
    """

    description = models.CharField('название контрольного выезда', max_length=300, blank=True, null=True)
    date = models.DateTimeField('дата загрузки файла на детектирование')
    video = models.FileField('Загруженный видео файл', upload_to='upload_video/', blank=True, null=True)
    count_pothole = models.IntegerField('колличество найденных ям', null=True, blank=True)
    count_image = models.IntegerField('колличество сохраненных изображении', null=True, blank=True)
    creator = models.ForeignKey(CustomUser, verbose_name='создатель', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='run_creator')

    def __str__(self):
        return str(self.date)
    
    class Meta:
        verbose_name = 'Таблица с данными о каждом выезде'
        verbose_name_plural = 'Таблица с данными о каждом выезде'


class Pothole(models.Model):
    url = models.FileField()
    latitude = models.FloatField('широта расположения ямы', null=True, blank=True)
    longitude = models.FloatField('долгота расположения ямы', null=True, blank=True)
    count_img_pothole = models.IntegerField('колличество ям на изображении', null=True, blank=True)
    date_table_id = models.ForeignKey(DetectedTable, on_delete=models.CASCADE, related_name='pothols')

    def __str__(self):
        return str(self.url.url)

    class Meta:
        verbose_name = 'Таблица с данными о каждой найденной яме'
        verbose_name_plural = 'Таблица с данными о каждой найденной яме'


class TrackerData(models.Model):
    """
    Таблица с данными от ГЛОНАСС трекера
    """

    latitude = models.FloatField()
    longitude = models.FloatField()
    navigationtime = models.DateTimeField()
    imei = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Таблица с данными полученные от ГЛОНАСС трекера'
        verbose_name_plural = 'Таблица с данными полученные от ГЛОНАСС трекера'