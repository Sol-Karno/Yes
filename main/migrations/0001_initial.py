# Generated by Django 4.1.2 on 2022-12-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Мероприятие')),
                ('opis', models.CharField(max_length=150, verbose_name='Описание мероприятия')),
                ('prise', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(max_length=50, verbose_name='Логин')),
                ('password', models.IntegerField(verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Авторизация',
                'verbose_name_plural': 'Авторизация',
            },
        ),
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(max_length=50, verbose_name='Логин')),
                ('password', models.IntegerField(verbose_name='Пароль')),
                ('password2', models.IntegerField(verbose_name='Повторите пароль')),
            ],
            options={
                'verbose_name': 'Регистрация',
                'verbose_name_plural': 'Регистрация',
            },
        ),
    ]
