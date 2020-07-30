from invite.models import Invite, InviteRegistration
from api.serializers.invites import InviteSerializer, InviteRegistrationSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5


class InviteViewSet(ModelViewSet):
    serializer_class = InviteSerializer
    queryset = Invite.objects.all()
    pagination_class = LargeResultsSetPagination


class InviteRegistrationViewSet(ModelViewSet):
    serializer_class = InviteRegistrationSerializer
    queryset = InviteRegistration.objects.all()
    pagination_class = LargeResultsSetPagination
