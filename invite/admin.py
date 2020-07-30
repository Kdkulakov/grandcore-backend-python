from django.contrib import admin
from .models import InviteRegistration, Invite


@admin.register(InviteRegistration)
class InviteRegistrationAdmin(admin.ModelAdmin):
    fields = ['id_invite', 'id_account']


@admin.register(Invite)
class InviteAdmin(admin.ModelAdmin):
    fields = ['uuid', 'registration', 'capacity', 'remaining_volume']
