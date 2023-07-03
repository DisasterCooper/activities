from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(blank=False, max_length=30)
    last_name = models.CharField(blank=False, max_length=50)

    class Meta:
        db_table = "user"
