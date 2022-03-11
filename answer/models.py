from django.db import models
from tasks.models import Task


class Answer(models.Model):
    description = models.TextField(verbose_name='описание ответа', null=True, blank=True)
    replyDate = models.DateTimeField(verbose_name='дата получения ответа', auto_now=True)
    task = models.ForeignKey(Task, verbose_name='связанная задача', on_delete=models.CASCADE, related_name='answer')

    def __str__(self):
        return self.description.__str__()

    class Meta:
        ordering = ('-replyDate',)
        verbose_name = 'Таблица с описанием ответа'
        verbose_name_plural = 'Таблица с описанием ответа'


class AnswerImages(models.Model):
    url = models.ImageField(upload_to='task_answer/', blank=True, null=True)
    answer = models.ForeignKey(Answer, verbose_name='ответ', null=True, blank=True,
                               on_delete=models.CASCADE,
                               related_name='answerimages')

    def get_url(self):
        return 'http://127.0.0.1:8000' + self.url.url

    def __str__(self):
        return self.url.url

    class Meta:
        verbose_name = 'Таблица с изображениями ответа'
        verbose_name_plural = 'Таблица с изображениями ответа'
