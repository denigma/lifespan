import lifespan
from grids import *
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from grids.views import *
from grids.viewsets import *
from grids.views import GridView, CoffeeModelView

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers


#router registers urlspatterns for REST
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'member', MemberViewSet)

urlpatterns = patterns('prototype.views',
                       url(r'^$', TemplateView.as_view(template_name="index.html")),
                       url(r'^page/(?P<num>\d{1})$', TemplateView.as_view(template_name="page.html")),

    )
