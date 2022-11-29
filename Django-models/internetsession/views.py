from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# add index func to show test html file
def index(request):
    template = loader.get_template('showtable.html')
    return HttpResponse(template.render())