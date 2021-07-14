from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel


class CustomUser(TimeStampedModel, AbstractUser):
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
