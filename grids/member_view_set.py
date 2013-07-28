from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework import *
from grids import serializers
from serializers import MemberSerializer
from grids.models import *

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import clone_request
import warnings
import django_filters
from django_filters import *
from rest_framework import filters


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter,)
    #fields that can be filtered
    filter_fields = ['id','name', 'surname', 'organization', 'age', 'salary']
    #fields that can be searched
    search_fields = filter_fields