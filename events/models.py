from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
    name = models.CharField(max_length=50)
    meeting_time = models.DateTimeField()
    description = models.CharField(max_length=250)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="events")
