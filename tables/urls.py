from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import lifespan

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^$', 'tables.views.index', name='index'),

                       url(r'^data/$', 'tables.views.data', name='index'),

                       #url(r'^html/.+$', 'lifespan.views.blank', name='index'),

                       url(r'^admin/', include(admin.site.urls)),
                       )
