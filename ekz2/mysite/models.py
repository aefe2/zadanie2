from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=150, verbose_name='Логин', unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=150, verbose_name='Логин', blank=True)
    last_name = models.CharField(max_length=150, verbose_name='Логин', blank=True)
    password = models.CharField(max_length=150, null=False, verbose_name='Пароль')


class Services(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название', blank=False)
    description = models.CharField(max_length=150, verbose_name='Описание', blank=False)
