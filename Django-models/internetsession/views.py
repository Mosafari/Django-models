from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import internet_seesion

# add index func to show test html file
def index(request):
    results = internet_seesion.objects.all()
    template = loader.get_template('showtable.html')
    return HttpResponse(template.render({'results': results}))