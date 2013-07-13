from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^table$', 'lifespan.views.table', name='index'),

    url(r'^table$', 'lifespan.views.table', name='table'),

    url(r'^chat$', 'lifespan.views.chat', name='chat'),

    url(r'^$', 'lifespan.views.index', name='index'),

    url(r'^lifespan$', 'lifespan.views.index', name='index'),


    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
