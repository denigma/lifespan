from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^chat$', 'lifespan.views.chat', name='chat'),
    url(r'^chats$',  TemplateView.as_view(template_name='chats.html'), name='chats'),

    url(r'^$', 'lifespan.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
