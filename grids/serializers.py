from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import *

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id','name', 'surname', 'organization', 'age', 'salary',)
