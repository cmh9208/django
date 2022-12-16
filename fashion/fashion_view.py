import json

from django.http import JsonResponse, QueryDict
from django.shortcuts import render
from matplotlib import pyplot as plt
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from fashion.fashion_service import FashionService
from shop.ir.iris import Iris
from shop.ir.iris_service import IrisService

# @api_view(["POST"])
# def fashion(request):
#     print(" ######## POST at Here ! ########  ")
#     body = request.body  # byte string of JSON data
#     print(f" ######## request.body is {body} ########  ")
#     data = json.loads(body)  # json to dict
#     print(request.headers)  # request의 header 정보
#     print(request.content_type)  # application/json
#     print(f"######## React ID is {data} ########")
#     result = FashionService().service_model(int(data['test_num']))
#     resp = ""
#     if result == 0:
#         resp = 'T-shirt/top'
#     elif result == 1:
#         resp = 'Trouser'
#     elif result == 2:
#         resp = 'Pullover'
#     elif result == 3:
#         resp = 'Dress'
#     elif result == 4:
#         resp = 'Coat'
#     elif result == 5:
#         resp = 'Sandal'
#     elif result == 6:
#         resp = 'Shirt'
#     elif result == 7:
#         resp = 'Sneaker'
#     elif result == 8:
#         resp = 'Bag'
#     elif result == 9:
#         resp = 'Ankle'
#     return JsonResponse({'resp': resp})
#
# @api_view(["GET"])
# def fashion(request, test_num):
#     print(" ######## GET at Here ! ########  ")
#     return JsonResponse(
#         {'result': FashionService().service_model(int(request.GET['test_num']))})

@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def fashion(request):
    if request.method == 'GET':
        print(f"######## test_num is {request.GET['test_num']} ########")
        return JsonResponse(
            {'result': FashionService().service_model(int(request.GET['test_num']))})

    elif request.method == 'POST':
          print(" ######## POST at Here ! ########  ")
          body = request.body  # byte string of JSON data   request.body로 리액트에서 넘어온 데이터를 쿼리딕으로 바꿈
          print(f" ######## request.body is {body} ########  ")
          data = json.loads(body)  # json to dict
          print(request.headers)  # request의 header 정보
          print(request.content_type)  # application/json
          print(f"######## React ID is {data} ########")
          result = FashionService().service_model(int(data['test_num']))
          resp = ""
          if result == 0:
              resp = 'T-shirt/top'
          elif result == 1:
              resp = 'Trouser'
          elif result == 2:
              resp = 'Pullover'
          elif result == 3:
              resp = 'Dress'
          elif result == 4:
              resp = 'Coat'
          elif result == 5:
              resp = 'Sandal'
          elif result == 6:
              resp = 'Shirt'
          elif result == 7:
              resp = 'Sneaker'
          elif result == 8:
              resp = 'Bag'
          elif result == 9:
              resp = 'Ankle'
          return JsonResponse({'resp': resp})






# @api_view(['POST'])
# @parser_classes([JSONParser])
# def fashion(request):
#     service = FashionService()
#     data = request.data
#     test_num = tf.constant(int(data['test_num']))
#     result = service.service_model(test_num)
#     print(f'리액트에서 보낸 데이터: {data}')
#     resp = ""
#     if result == 0:
#         resp = 'T-shirt/top'
#     elif result == 1:
#         resp = 'Trouser'
#     elif result == 2:
#         resp = 'Pullover'
#     elif result == 3:
#         resp = 'Dress'
#     elif result == 4:
#         resp = 'Coat'
#     elif result == 5:
#         resp = 'Sandal'
#     elif result == 6:
#         resp = 'Shirt'
#     elif result == 7:
#         resp = 'Sneaker'
#     elif result == 8:
#         resp = 'Bag'
#     elif result == 9:
#         resp = 'Ankle'
#     # 상태없음(무상태) = 딕셔너리 사용
#     # 무조건 딕셔너리 사용 = 보안을위해
#     # 대문자로 시작 = 생성자
#     # 리스트로 할때 {[]}
#     # 생성자는 Json 객체는 Response
#     # 무상태 프로그래밍 = {} 를 Response객체에 담아 보냄
#     # {}를 객체에 담아야지만 암호화
#     # 위처럼 하면 메모리 상수풀에 담김
#     # 세션을 안써서 무상태 프로그래밍
#     # 장고에선 제이슨 리액트에선 딕셔너리
#     return JsonResponse({'resp': resp})
#     # return resp 무상태 아님


# ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
#                        'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


# @api_view(['GET'])
# def fashion(request):
#
#     if request.method == 'GET':
#         body = request.body
#         data = json.loads(body)
#         print(request.headers)
#         print(request.content_type)
#         print(f'##### React ID is {data} ######')
#         service = FashionService()
#         resp = 'TEST SUCCESS !'
#         return JsonResponse({"resp":resp} )
#     else:
#         print(f'##### React ID is None ######')
################################################################################


