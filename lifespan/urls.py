from django.conf.urls import patterns, include, url
from django.contrib import admin
from lifespan.admin import *
import rest_framework_swagger
from grids.views import GridView,CoffeeModelView
from django.views.generic import TemplateView

## REST Framework
from rest_framework import routers
# from account.rest import UserViewSet, GroupViewSet
from lifespan.rest import (StudyViewSet, ExperimentViewSet, StrainViewSet,
                           MeasurementViewSet, EpistasisViewSet, ComparisonViewSet,
                           ManipulationViewSet, RegimenViewSet, AssayViewSet, InterventionViewSet,
                           FactorViewSet, TypeViewSet, StateViewSet,  TechnologyViewSet,
                           StudyTypeViewSet, VariantTypeViewSet, ORTypeViewSet, PopulationViewSet,
                           VariantViewSet, GenderViewSet)


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)
router.register(r'studies', StudyViewSet)
router.register(r'experiments', ExperimentViewSet)
router.register(r'strains', StrainViewSet)
router.register(r'measurements', MeasurementViewSet)
router.register(r'epistases', EpistasisViewSet)
router.register(r'manipulations', ManipulationViewSet)
router.register(r'regimens', RegimenViewSet)
router.register(r'assays', AssayViewSet)

router.register(r'interventions', InterventionViewSet)
router.register(r'factors', FactorViewSet)
router.register(r'types', TypeViewSet)
router.register(r'states', StateViewSet)
router.register(r'technologies', TechnologyViewSet)
router.register(r'studytypes', StudyTypeViewSet)
router.register(r'varianttypes', VariantTypeViewSet)
router.register(r'or-types', ORTypeViewSet)
router.register(r'populations', PopulationViewSet)
router.register(r'variants', VariantViewSet)
router.register(r'genders', GenderViewSet)

admin.autodiscover()


urlpatterns = patterns('',
    #(r'^$', RedirectView.as_view(url='/grids/')), #redirect to the most used app
    #url(r'^Member/(.+)$', 'grids.views.test', name='index'),
    #url(r'^$', 'lifespan.views.interventions', name='index'),
    url(r'^selectable/', include('selectable.urls')),

    url(r'^$', TemplateView.as_view(template_name="interventions.html")),


    url(r'^$', GridView.as_view(template_name="grid.html",model_name="Member")),


    url(r'^grids/', include('grids.urls', namespace="grids")),
    url(r'^tables/' , include('tables.urls', namespace="tables")),
    url(r'^chat/', include('chats.urls', namespace="chats")),

    url(r'^models/', include(router.urls)),


    url(r'^prototype/', include('prototype.urls', namespace="grids")),


    url(r'^admin/', include(admin.site.urls)),

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api-docs/', include('rest_framework_swagger.urls')),

    url(r'^lifespan/', TemplateView.as_view(template_name='interventions.html')),

    #url(r'^variants/', GridView.as_view(template_name="variant.html",model_name="Variant")),


    # url(r'^variants/', GridView.as_view(template_name="variant.html",model_name="organization")),


    url(r'^$', GridView.as_view(template_name="grid.html",model_name="Member")),


    )
