from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

class Todo(models.Model):
    user = models.ForeignKey(User, null=True, default=None)

    text = models.CharField(max_length=100, blank=False)
    done = models.BooleanField(default=False)

    timestamp = models.DateTimeField(default=datetime.now, null=False)
