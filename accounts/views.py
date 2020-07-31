from rest_framework.decorators import api_view, APIView
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django.template import loader
from django.views.generic import TemplateView
from django.http import JsonResponse

import datetime
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10


def send_mail(to, context):
    html_content = render_to_string('accounts/email/activate_profile.html', context)
    text_content = render_to_string('accounts/email/activate_profile.txt', context)

    msg = EmailMultiAlternatives(context['subject'], text_content, settings.DEFAULT_FROM_EMAIL, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def create_mail(nfcid, readerid):
    print(readerid)
    try:
        guest = Guest.objects.get(nfc_id=nfcid)
        print(guest.email)
    except Exception:
        print("Not found Guest with " + nfcid + " NFC ID.")
        return
    guest = Guest.objects.get(nfc_id=nfcid)
    reader_instance = ReaderId.objects.get(valueid=readerid)
    stand_instance = Stand.objects.get(reader=reader_instance)

    add_new_mail = MailRecord.objects.create(stand=stand_instance, guest=guest)
    add_new_mail.save()

    context = {
        'subject': stand_instance.name,
        'body': stand_instance.desc
    }
    try:
        send_mail(guest.email, context)
    except Exception as err:
        print(str(err))
    return

