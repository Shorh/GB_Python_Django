from django.db import models
from django.contrib.auth.models import AbstractUser


class AccountUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='accounts',
        blank=True,
        null=True,
    )

    phone = models.CharField(
        max_length=13,
        blank=True,
        null=True,
    )

    def __set__(self):
        return self.username
