from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    name = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
