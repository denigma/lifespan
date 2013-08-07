from django.conf.urls import patterns, url

from django.views.generic import TemplateView

from views import ImageView, DeleteImage

## REST Framework
from rest_framework import routers
from rest import ImageViewSet

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'images', ImageViewSet)

urlpatterns = patterns('media.views',
    url(r'^$', 'index', name='media'),
    url(r'^slides', TemplateView.as_view(template_name='gallery/slides.html'), name='slides'),
    url(r'^(?P<pk>\d+)', ImageView.as_view(), name='detail-image'),
    url(r'^delete/(?P<pk>\d+)', DeleteImage.as_view(), name='delete-image'),
    url(r'^prezi', TemplateView.as_view(template_name='gallery/prezi.html'), name='prezi')
)