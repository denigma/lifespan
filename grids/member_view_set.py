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
    filter_fields = ['id','name', 'surname', 'organization', 'age', 'salary']
    search_fields = filter_fields

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = self.queryset
    #     #keys = Member.objects.all()[0].keys()
    #     name = self.request.QUERY_PARAMS.get("name", None)
    #     surname = self.request.QUERY_PARAMS.get("surname", None)
    #     organization = self.request.QUERY_PARAMS.get("organization", None)
    #     age = self.request.QUERY_PARAMS.get("age", None)
    #     salary = self.request.QUERY_PARAMS.get("salary", None)
    #     if name == None:
    #         queryset = queryset.filter(surname__contains=surname)
    #     if surname == None:
    #         queryset = queryset.filter(surname__contains=surname)
    #     if organization == None:
    #         queryset = queryset.filter(surname__contains=surname)
    #     if age == None:
    #         queryset = queryset.filter(age=age)
    #
    #     return queryset

    # def list(self, request, *args, **kwargs):
    #     self.object_list = self.filter_queryset(self.get_queryset())
    #
    #     # Default is to allow empty querysets.  This can be altered by setting
    #     # `.allow_empty = False`, to raise 404 errors on empty querysets.
    #     if not self.allow_empty and not self.object_list:
    #         warnings.warn(
    #             'The `allow_empty` parameter is due to be deprecated. '
    #             'To use `allow_empty=False` style behavior, You should override '
    #             '`get_queryset()` and explicitly raise a 404 on empty querysets.',
    #             PendingDeprecationWarning
    #         )
    #         class_name = self.__class__.__name__
    #         error_msg = self.empty_error % {'class_name': class_name}
    #         raise Http404(error_msg)
    #
    #     # Switch between paginated or standard style responses
    #     page = self.paginate_queryset(self.object_list)
    #     if page is not None:
    #         serializer = self.get_pagination_serializer(page)
    #     else:
    #         serializer = self.get_serializer(self.object_list, many=True)
    #
    #     return Response(serializer.data)
