from django.contrib import admin
from ..models import (
    Feedback
)

class FeedbackAdmin(admin.ModelAdmin):
    fields = ("title", "description", "rating")
    list_display = ("title", "description", "rating")


feedback = admin.site.register(Feedback, FeedbackAdmin)