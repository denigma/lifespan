from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import *

#this class works with member serialization and deserialization
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id','name', 'surname', 'organization', 'age', 'salary',)
