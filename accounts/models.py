from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Добавим поле для хранения дополнительной информации о пользователе
    bio = models.TextField(blank=True)
