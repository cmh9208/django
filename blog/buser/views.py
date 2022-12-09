from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser


# Create your views here.
@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    print(f'Enter Blog-Login with {request}')
    return JsonResponse({'Response Test' : 'SUCCESS'})