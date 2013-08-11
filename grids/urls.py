import lifespan
from grids import *
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from grids.views import *
from grids.member_view_set import *
from grids.views import GridView, CoffeeModelView

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers


#router registers urlspatterns for REST
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'member', MemberViewSet)

urlpatterns = patterns('grids.views',
    url(r'fixture/', 'fixture', name='fixture'),
    url(r'models/', include(router.urls)),

    url(r'^coffee/',CoffeeModelView.as_view(template_name="model_coffee.html",model_name="Member")),

    url(r'^$', GridView.as_view(template_name="grid.html",model_name="Member")),

    url(r'^admin/', include(admin.site.urls)),
    )
