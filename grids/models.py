# -*- coding: utf-8 -*-
from django.db import models


class Organization(models.Model):
    """Testing model to test grids"""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    # # This functions maybe redundant.
    # # I added them as I did not know how to get all model fields and values as dictionaries
    @classmethod
    def keys(cls): return [field.name for field in cls._meta.fields]

    @classmethod
    def values(cls): return [getattr(cls, field.name) for field in cls._meta.fields]

    @classmethod
    def items(cls): return {field.name:getattr(cls, field.name) for field in cls._meta.fields}

class Member(models.Model):
    """Testing model to test grids"""
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization)#models.CharField(max_length=255)
    age = models.IntegerField()
    salary = models.FloatField()

    # # This functions maybe redundant.
    # # I added them as I did not know how to get all model fields and values as dictionaries
    @classmethod
    def keys(cls): return [field.name for field in cls._meta.fields]

    @classmethod
    def values(cls): return [getattr(cls, field.name) for field in cls._meta.fields]

    @classmethod
    def items(cls): return {field.name:getattr(cls, field.name) for field in cls._meta.fields}
