# Generated by Django 3.0.8 on 2020-07-30 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invite', '0002_auto_20200730_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inviteregistration',
            old_name='user',
            new_name='id_account',
        ),
    ]
