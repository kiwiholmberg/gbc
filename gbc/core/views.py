from django.shortcuts import render
from django.conf import settings
from core.models import Slide, Tile, Menu_item, Featurette


def home(request):
    slides = Slide.objects.all()
    tiles = Tile.objects.all()
    menu_items = Menu_item.objects.all()
    featurettes = Featurette.objects.all()

    lang = request.COOKIES.get('language', 'sv')
    return render(request, 'index.html', {  'STATIC_URL': settings.STATIC_URL, 
                                            'slides': slides,
                                            'tiles': tiles, 
                                            'menu_items': menu_items, 
                                            'featurettes': featurettes,
                                            'lang': lang
                                        })