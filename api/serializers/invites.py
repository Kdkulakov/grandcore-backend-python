from rest_framework.serializers import ModelSerializer
from invite.models import Invite, InviteRegistration


class InviteSerializer(ModelSerializer):

    class Meta:
        model = Invite
        fields = "__all__"


class InviteRegistrationSerializer(ModelSerializer):

    class Meta:
        model = InviteRegistration
        fields = "__all__"