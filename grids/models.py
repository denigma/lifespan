# -*- coding: utf-8 -*-
from django.db import models


class Member(models.Model):
    """Testing model to test grids"""
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    age = models.IntegerField()
    salary = models.FloatField()


    # This functions maybe redundant.
    # I added them as I did not know how to get all model fields and values as dictionaries
    def keys(self): return [field.name for field in self._meta.fields]

    def values(self): return [getattr(self, field.name) for field in self._meta.fields]

    def items(self): return {field.name:getattr(self, field.name) for field in self._meta.fields}

