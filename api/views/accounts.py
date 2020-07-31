from accounts.models import Account
from invite.models import Invite, InviteRegistration
from api.serializers.accounts import AccountSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5


class AccountViewSet(ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    pagination_class = LargeResultsSetPagination


def check_invite_not_empty(invite):
    invite_obj = Invite.objects.get(uuid=invite)

    if invite_obj.capacity > 0 and invite_obj.remaining_volume <= invite_obj.capacity:
        if invite_obj.remaining_volume > 0:
            invite_obj.remaining_volume = invite_obj.remaining_volume - 1
            invite_obj.save()
            print('Minus odna registraciya')
            return True
        else:
            return False
    else:
        return False


def check_invite_exists(invite):
    try:
        Invite.objects.get(uuid=invite)
        return True
    except Exception:
        return False


def create_user(email, password, invite):
    try:
        Account.objects.get(email=email)
        return HttpResponse('Uzver this email exist', 403)
    except Exception:
        user_id = Account.objects.create_user(email, password)
        user_id.is_active = False
        user_id.save()
        print(user_id.email + " " + str(user_id.id))

        create_invite_registration(invite, user_id)

    return user_id.id


def create_invite_registration(invite, user_id):
    invite_obj = Invite.objects.get(uuid=invite)
    inv_reg_obj = InviteRegistration.objects.create(id_invite=invite_obj, id_account=user_id)
    inv_reg_obj.save()
    print(f'User {user_id.email} with invite - {invite} was registered: {inv_reg_obj.id}')
    user_id.is_active = True
    user_id.save()
    print(f'User {user_id.email} - ACITVATE')
    return


@api_view(['POST'])
@permission_classes([AllowAny])
def account_registration_handler(request):

    if request.method == 'POST':
        try:
            request.data['email']
        except Exception:
            return HttpResponse('No email field in request', 403)

        try:
            request.data['password']
        except Exception:
            return HttpResponse('No password field in request', 403)

        try:
            request.data['invite']
        except Exception:
            return HttpResponse('No ivite field in request', 403)

        email = request.data['email']
        password = request.data['password']
        invite = request.data['invite']

        if check_invite_exists(invite):
            if check_invite_not_empty(invite):
                user_id = create_user(email, password, invite)

                return HttpResponse(user_id, 200)
            else:
                return HttpResponse('Invite is empty, give new', 200)
        else:
            return HttpResponse('Invite not exists', 404)

    return HttpResponse('Some error', 500)