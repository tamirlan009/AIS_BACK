from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.login = None

    is_company_employee = models.BooleanField(verbose_name='Роль сотрудника компании',
                                              help_text='Отметьте, если пользователь может создовать поручения для подрядчиков',
                                              default=False)
    is_contractor = models.BooleanField(verbose_name='Роль подрядчика',
                                        help_text='Отметьте, если пользователь явяеться подрядчиком', default=False)
    number_phone = PhoneNumberField(verbose_name='номер телефона пользователья', blank=True, null=True)


