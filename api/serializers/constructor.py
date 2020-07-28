from rest_framework.serializers import ModelSerializer
from constructor.models import Course, Training, TrainingSet, TrainingPassRecord, CourseRegistrationRecord


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class TrainingSerializer(ModelSerializer):

    class Meta:
        model = Training
        fields = "__all__"


class TrainingSetSerializer(ModelSerializer):

    class Meta:
        model = TrainingSet
        fields = "__all__"


class TrainingPassRecordSerializer(ModelSerializer):

    class Meta:
        model = TrainingPassRecord
        fields = "__all__"


class CourseRegistrationRecordSerializer(ModelSerializer):

    class Meta:
        model = CourseRegistrationRecord
        fields = "__all__"
