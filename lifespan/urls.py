from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from tables import *
from grids import *
from chats import *
from django.http import HttpResponseRedirect
from django.contrib import admin
admin.autodiscover()

from django.views.generic import RedirectView

urlpatterns = patterns('',

    (r'^$', RedirectView.as_view(url='/grids/')), #redirect to the most used app

    url(r'^grids/', include('grids.urls', namespace="grids")),
    url(r'^tables/' , include('tables.urls', namespace="tables")),
    url(r'^chat/', include('chats.urls', namespace="chats")),

    url(r'^$', 'lifespan.views.index', name='index'),
    url(r'^lifespan/', 'lifespan.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
