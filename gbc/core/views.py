from django.shortcuts import render
from django.conf import settings
from core.models import Slide


def home(request):
    slides = Slide.objects.all()
    return render(request, 'index.html', { 'STATIC_URL': settings.STATIC_URL, 'slides':slides })