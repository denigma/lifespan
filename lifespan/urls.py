from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import rest_framework_swagger

from rest_framework import routers
from lifespan import views

router = routers.DefaultRouter()
router.register(r'members', views.MemberViewSet)


urlpatterns = patterns('',
    #(r'^$', RedirectView.as_view(url='/grids/')), #redirect to the most used app
    #url(r'^Member/(.+)$', 'grids.views.test', name='index'),
    url(r'^api/', include(router.urls)),

    url(r'^grids/', include('grids.urls', namespace="grids")),
    url(r'^tables/' , include('tables.urls', namespace="tables")),
    url(r'^chat/', include('chats.urls', namespace="chats")),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api-docs/', include('rest_framework_swagger.urls')),

    url(r'^$', 'lifespan.views.index', name='index'),
    url(r'^lifespan/', 'lifespan.views.index', name='index'),

    )
