from django.db import models

from project.core.models import BaseModel
# from django.contrib.postgres.fields import ArrayField


class Country(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'


class State(BaseModel):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=2, blank=True, null=True)
    country = models.ForeignKey(Country, related_name='country', on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'States'