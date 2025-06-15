from django.utils.translation import gettext_lazy as _

from django.db import models
from django.conf import settings

from django.db import models


class Feedback(models.Model):
    title = models.CharField(max_length = 40)
    description = models.CharField(max_length=256, null=True)
    rating = models.FloatField(null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    product = models.ForeignKey(
        to = "Product",
        on_delete = models.CASCADE,
        related_name = "feedbacks",
        blank = True,
        null = True,
    )

    user = models.ForeignKey(
        to = settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name='feedbacks',
        blank = True,
        null = True,

    )

