from django.urls import path
from . import views


# add path of index to urlpatterns 
# adding tableApiView to urlpatterns
urlpatterns = [
    path('', views.index, name='index'),
    path('api', views.records),
]