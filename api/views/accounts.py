from accounts.models import Account
from api.serializers.accounts import AccountSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5


class AccountViewSet(ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    pagination_class = LargeResultsSetPagination