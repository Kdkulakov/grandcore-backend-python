# Generated by Django 3.0.8 on 2020-07-30 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('registration', models.PositiveSmallIntegerField(verbose_name='количество егистраций')),
                ('capacity', models.PositiveSmallIntegerField(verbose_name='объем регистраций')),
                ('remaining_volume', models.PositiveSmallIntegerField(verbose_name='остаток регистраций')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InviteRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id_invite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invite.Invite', verbose_name='инвайт регистрации')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]
