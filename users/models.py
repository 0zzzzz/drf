from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    email = models.EmailField(max_length=70, unique=True, **NULLABLE)

    def __str__(self):
        return f'{self.username} ({self.last_name} {self.first_name})'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
