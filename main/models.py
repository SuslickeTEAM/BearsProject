from django.db import models


class Images(models.Model):
    url = models.CharField('Url', max_length=100)