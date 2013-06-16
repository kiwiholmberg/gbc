# encoding: utf-8
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest,HttpResponseServerError
from django.conf import settings
from mailsnake import MailSnake
from mailsnake.exceptions import *
import re

def newsletter_signup(request):
    email = request.POST['email']

    if re.match('^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$', email):
        ms = MailSnake(settings.MAILCHIMP_KEY)
        r = ms.listSubscribe(id='df179acee6', email_address=email)
        print(r)
        if r:
            return HttpResponse()  
        else:
            return HttpResponseServerError()
    else:
        #Invalid email address. Return 400        
        return HttpResponseBadRequest(content='Invalid email address')