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

                       url(r'^$', 'chats.views.index', name='index'),

                       url(r'^admin/', include(admin.site.urls)),
                       )
