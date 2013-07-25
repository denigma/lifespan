from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Member


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('name', 'surname', 'organization', 'age', 'salary',)