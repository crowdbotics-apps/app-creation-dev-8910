from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    fk_to_user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        default=1,
        on_delete=models.SET_DEFAULT,
        related_name="customtext_fk_to_user",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    jkjk = models.OneToOneField(
        "home.CustomText",
        null=True,
        blank=True,
        default=1,
        on_delete=models.SET_DEFAULT,
        related_name="homepage_jkjk",
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class NewModel(models.Model):
    "Generated Model"
    field = models.CharField(max_length=256,)
