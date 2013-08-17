from rest_framework.serializers import SlugRelatedField,ModelSerializer
from models import Member,Organization

class  MemberSerializer(ModelSerializer):
    organization = SlugRelatedField(slug_field='name')

    class Meta:
        model = Member
