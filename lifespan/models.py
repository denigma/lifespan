# -*- coding: utf-8 -*-
from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    age = models.IntegerField()
    salary = models.FloatField()

