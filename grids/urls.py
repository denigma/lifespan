import lifespan
from grids import *
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from grids.views import *
from grids.member_view_set import *

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers


#router registers urlspatterns for REST
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'member', MemberViewSet)

urlpatterns = patterns('grids.views',
    url(r'fixture/', 'fixture', name='fixture'),
    url(r'models/', include(router.urls)),
    url(r'^$', 'index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
    )
