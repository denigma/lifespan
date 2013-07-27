import lifespan
from grids import *
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from grids.views import *

from django.contrib import admin
admin.autodiscover()


from rest_framework import routers
from lifespan import views

#router registers urlspatterns for REST
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'member', MemberViewSet)

urlpatterns = patterns('',
    url(r'models/test/member/', 'grids.views.members', name='members'),
    url(r'models/', include(router.urls)),
    url(r'^$', 'grids.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
    )
