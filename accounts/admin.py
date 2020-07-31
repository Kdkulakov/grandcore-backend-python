from accounts.models import Account, AccountGroup


"""Integrate with admin module."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _


@admin.register(Account)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'second_name', 'last_name', 'group',  'skills', 'occupation', 'avatar',
                                          'about', 'phone', 'is_deleted')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_deleted')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    list_filter = [
        'skills'
    ]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags_list')

    def tags_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())



@admin.register(AccountGroup)
class AccountGroupAdmin(admin.ModelAdmin):
    fields = ['name']