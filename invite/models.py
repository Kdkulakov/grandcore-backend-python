from django.db import models
import uuid
from accounts.models import Account


class Invite(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    registration = models.PositiveSmallIntegerField(
        verbose_name='количество егистраций'
    )
    capacity = models.PositiveSmallIntegerField(
        verbose_name='объем регистраций'
    )
    remaining_volume = models.PositiveSmallIntegerField(
        verbose_name='остаток регистраций'
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return str(self.uuid) or ''


class InviteRegistration(models.Model):
    id_invite = models.ForeignKey(
        Invite,
        on_delete=models.CASCADE,
        verbose_name='инвайт регистрации'
    )
    id_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name='пользователь'
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return str(self.id_invite) + " " + self.user or ''