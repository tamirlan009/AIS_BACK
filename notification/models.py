from django.db import models
from users.models import CustomUser


class NotificationTable(models.Model):
    """
    Таблица с увиедомлениями
    """
    message = models.CharField('текст уведоления', max_length=300)
    recipient = models.ForeignKey(CustomUser, verbose_name='Получатель уведомления',
                                  on_delete=models.CASCADE, related_name='recipient_user')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Таблица с уведомлениями'
        verbose_name_plural = 'Таблица с уведомлениями'