# Generated by Django 4.0.2 on 2022-03-10 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300, verbose_name='текст уведоления')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient_user', to=settings.AUTH_USER_MODEL, verbose_name='Получатель уведомления')),
            ],
            options={
                'verbose_name': 'Таблица с уведомлениями',
                'verbose_name_plural': 'Таблица с уведомлениями',
            },
        ),
    ]
