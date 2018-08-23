from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    image = models.ImageField(blank=True)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.username


