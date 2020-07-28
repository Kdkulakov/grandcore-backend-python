from rest_framework.serializers import ModelSerializer
from accounts.models import Account, UserBMIRecord, UserWeightRecord, UserHeightRecord


class AccountSerializer(ModelSerializer):

    class Meta:
        model = Account
        fields = "__all__"


class UserWeightRecordSerializer(ModelSerializer):

    class Meta:
        model = UserWeightRecord
        fields = "__all__"


class UserHeightRecordSerializer(ModelSerializer):

    class Meta:
        model = UserHeightRecord
        fields = "__all__"


class UserBMIRecordSerializer(ModelSerializer):

    class Meta:
        model = UserBMIRecord
        fields = "__all__"


