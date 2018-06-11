from django.db import models


class Shortly(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField(unique=True)
    clicked = models.IntegerField(default=0)
