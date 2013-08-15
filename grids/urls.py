import lifespan
from grids import *
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from grids.views import *
from grids.viewsets import *
from grids.views import GridView, CoffeeModelView, SelectableGridView

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers


#router registers urlspatterns for REST
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'member', MemberViewSet)
router.register(r'organization', OrganizationViewSet)

urlpatterns = patterns('grids.views',
    url(r'^selectable/', include('selectable.urls')),
    url(r'^fixture/', 'fixture', name='fixture'),
    url(r'^models/', include(router.urls)),

    #this view allows us to generate controller coffees, named param needed
    url(r'^coffee/controller/$',CoffeeModelView.as_view(template_name="controller.coffee.html",model_name="Member",namespace = "grids")),

    #just for fun
    url(r'^controller/$',CoffeeModelView.as_view(template_name="controller.html",model_name="Member",namespace = "grids")),


    #generates typical coffeescript model
    url(r'^coffee/model/$',CoffeeModelView.as_view(template_name="model.coffee.html",model_name="Member",namespace = "grids")),

    #just for fun
    url(r'^model/$',CoffeeModelView.as_view(template_name="model.html",model_name="Member",namespace = "grids")),


    url(r'^$', SelectableGridView.as_view(template_name="grid.html",model_name="Member")),


    url(r'^admin/', include(admin.site.urls)),


    )
