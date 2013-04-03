from django.shortcuts import render
from django.conf import settings


def home(request):
    return render(request, 'index.html', { 'STATIC_URL': settings.STATIC_URL })