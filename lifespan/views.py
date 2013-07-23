import random

from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render


def index(request): return render(request, 'interventions.html')


