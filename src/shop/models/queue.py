from django.db import models
from django.db.models import PositiveIntegerField


class Queue(models.Model):
    value = models.PositiveIntegerField()
