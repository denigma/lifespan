import lifespan
import grids
from grids import *
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^$', 'grids.models.views.all', name='index'),

                       url(r'^(?P<uri>(.+))$', 'grids.models.views.save', name='save'),
                       )
