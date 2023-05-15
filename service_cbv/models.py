from django.db import models
from django.urls import reverse


class Service(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service_cbv:service_edit', kwargs={'pk': self.pk})