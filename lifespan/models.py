# -*- coding: utf-8 -*-
from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    age = models.IntegerField()
    salary = models.FloatField()

    def keys(self): return [field.name for field in self._meta.fields]

    def values(self): return [getattr(self, field.name) for field in self._meta.fields]

    def items(self): return {field.name:getattr(self, field.name) for field in self._meta.fields}

