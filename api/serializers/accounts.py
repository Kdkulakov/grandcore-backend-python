from rest_framework.serializers import ModelSerializer
from accounts.models import Account


from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)


class AccountSerializer(TaggitSerializer, ModelSerializer):
    skills = TagListSerializerField()

    class Meta:
        model = Account
        fields = "__all__"

