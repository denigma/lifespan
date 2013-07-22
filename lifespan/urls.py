from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^models/([a-zA-Z]+)$', 'lifespan.views.writeModel', name='index'),

    url(r'^$', 'lifespan.views.grid', name='index'),

    url(r'^Member$', 'lifespan.views.members', name='index'),

    url(r'^html/.+$', 'lifespan.views.blank', name='index'),

    url(r'^data', 'lifespan.views.load_table', name='table'),

    url(r'^messages', 'lifespan.views.messages', name='messages'),

    url(r'^table$', 'lifespan.views.table', name='table'),


    url(r'^chat$', 'lifespan.views.chat', name='chat'),

    url(r'^$', 'lifespan.views.index', name='index'),

    url(r'^lifespan$', 'lifespan.views.index', name='index'),


    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
