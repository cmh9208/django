from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from shop.ir.iris import Iris


# @api_view(['POST'])
# @parser_classes([JSONParser])
# def iris(request):
#     Iris().hook()
#     print(f'Enter show face with {request}')
#     return JsonResponse({'Response Test' : 'SUCCESS'})


@api_view(['POST'])
@parser_classes([JSONParser])
def iris(request):
    user_info = request.data

    petal_width = user_info['petal_width']
    petal_length = user_info['petal_length']

    sepal_width = user_info['sepal_width']
    sepal_length = user_info['sepal_length']

    print(f'리액트에서 보낸 데이터: {user_info}')

    print(f'넘어온 꽃잎 폭: {petal_width}')
    print(f'넘어온 꽃잎 길이: {petal_length}')

    print(f'넘어온 꽃받침 폭: {sepal_width}')
    print(f'넘어온 꽃받침 길이: {sepal_length}')

    print(f'Enter show face with {request}')
    return JsonResponse({'Response Test' : 'SUCCESS'})

