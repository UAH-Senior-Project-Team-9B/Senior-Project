from django.contrib.auth.models import Group
from django.db import models


class TokenAuthModel(models.Model):
    token = models.CharField(max_length=30, unique=True)
    time_created = models.DateTimeField().auto_now
    expiration = models.DateField()
    group = models.OneToOneField(to=Group, on_delete=models.CASCADE)
