from django.db import models
from django.urls import reverse

class Catalog(models.Model):
    title = models.CharField('Мероприятие', max_length=50)
    opis = models.CharField('Описание мероприятия', max_length=150)
    prise = models.IntegerField('Цена')

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural ="Мероприятия"

class Reg(models.Model):
    log = models.CharField('Логин', max_length=50)
    password = models.IntegerField('Пароль')
    password2 = models.IntegerField('Повторите пароль')

    def __str__(self):
        return self.log

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрация'

class Login(models.Model):
    log = models.CharField('Логин', max_length=50)
    password = models.IntegerField('Пароль')

    def __str__(self):
        return self.log

    class Meta:
        verbose_name = 'Авторизация'
        verbose_name_plural = 'Авторизация'

class user(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
