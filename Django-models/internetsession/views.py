from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import internet_seesion as IS
from .serializers import modelSerializer
# from django.http import

# add index func to show test html file
def index(request):
    results = IS.objects.all()
    template = loader.get_template('showtable.html')
    return HttpResponse(template.render({'results': results}))


@api_view(['GET','POST'])
def records(request):
    '''
    List all the table items for given requested user
    '''
    if request.method == 'GET':
        IS.objects.filter(ID=1644).delete()
        records = IS.objects.all()
        print("ok1")
        serializer = modelSerializer(records, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data,safe=False,)

# 2. Create
    print("done")
    if request.method == 'POST':
        '''
        Create new record with given data
        '''
        serializer = modelSerializer(data=request.data)
        print(Response())
        print("done",serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print("this" ,serializer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)