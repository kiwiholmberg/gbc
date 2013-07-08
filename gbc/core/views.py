from django.shortcuts import render
from django.conf import settings
from core.models import Slide, Tile, Menu_item, Featurette, Sponsor


def home(request):
    slides = Slide.objects.all().order_by('order')
    tiles = Tile.objects.all().order_by('order')
    menu_items = Menu_item.objects.all().order_by('order')
    featurettes = Featurette.objects.all().order_by('order')
    sponsors = Sponsor.objects.all().order_by('order')

    lang = request.COOKIES.get('language', 'sv')
    return render(request, 'index.html', {  'STATIC_URL': settings.STATIC_URL, 
                                            'slides': slides,
                                            'tiles': tiles, 
                                            'menu_items': menu_items, 
                                            'featurettes': featurettes,
                                            'lang': lang,
                                            'sponsors': sponsors,
                                        })