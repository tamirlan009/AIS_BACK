# Generated by Django 4.0.2 on 2022-03-10 13:09

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название категории')),
            ],
            options={
                'verbose_name': 'Таблица с категориями задач',
                'verbose_name_plural': 'Таблица с категориями задач',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True, verbose_name='описание задачи')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='широта местоположения')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='долгота местоположения')),
                ('address', models.TextField(blank=True, null=True, verbose_name='адрес местоположения')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='дата создания и отправки на выполнение')),
                ('leadTime', models.DateTimeField(blank=True, null=True, verbose_name='Срок выполнения')),
                ('is_done', models.BooleanField(default=False, verbose_name='задача выполнено или нет')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='tasks.category', verbose_name='категория задачи')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator', to=settings.AUTH_USER_MODEL, verbose_name='создатель')),
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='executor', to=settings.AUTH_USER_MODEL, verbose_name='исполнитель')),
            ],
            options={
                'verbose_name': 'Таблица с описанием задач',
                'verbose_name_plural': 'Таблица с описанием задач',
                'ordering': ('-createDate',),
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(blank=True, null=True, upload_to='single_task/')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tasks.task', verbose_name='связанная задача')),
            ],
            options={
                'verbose_name': 'Таблица с изображениями',
                'verbose_name_plural': 'Таблица с изображениями',
            },
        ),
    ]
