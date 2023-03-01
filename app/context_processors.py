from .models import *

def menu_links(request):
    links = Contact.objects.all()
    return dict(links=links)