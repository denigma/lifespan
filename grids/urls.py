import lifespan
import grids
from grids import *
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'grids.views.index', name='index'),
    #url(r'^models/(?P<model>([a-zA-Z_]+))$','grids.views.test',name="models"),
    url(r'^models/(?P<model>([a-zA-Z_]+))/?',include('grids.models.urls', namespace="models")),

    #url(r'^models/([a-zA-Z]+)$', 'grids.views.writeModel', name='index'),
    url(r'^Member/?$', 'grids.views.members', name='index'),
    #url(r'^html/.+$', 'lifespan.views.blank', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    )
