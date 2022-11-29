from django.urls import path
from . import views

# add path of index to urlpatterns 
urlpatterns = [
    path('', views.index, name='index'),
]