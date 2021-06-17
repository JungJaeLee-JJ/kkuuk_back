from .models import Store, Client, MemberShip
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# RestFramework
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken

import json

#response 메세지
def res_msg(code, msg, data={}) :
    return {'code':code, 'msg':msg , 'data':data}

class SignUp(APIView):
    def post(self, request, format=None):
        try:
            username = request.data['username']
            password = request.data['password']
            call = request.data['call']
            email = request.data['email']
            user = Store.objects.create_user(username=username, password=password, email=email, call=call)
            serializer = AuthTokenSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse(res_msg(200,'회원가입이 완료되었습니다.',{'token':token.key}))
        except Exception as e:
            print(e)
            return JsonResponse(res_msg(500, e.__str__()))

class DuplicateCheck(APIView):
    def post(self, request):
        try:
            email = request.data['email']
            store = Store.objects.filter(email=email)
            if store.exists():
                return JsonResponse(res_msg(200, '중복'))
            return JsonResponse(res_msg(200, '신규'))
        
        except Exception as e:
            return JsonResponse(res_msg(500, e.__str__()))

class LogIn(APIView):
    def post(self, request):
        try:
            user = Store.objects.get(username=request.data['username'])
            serializer = AuthTokenSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse(res_msg(200, '로그인에 성공하였습니다.',{'token':token.key}))
        except Exception as e:
            print(e)
            return JsonResponse(res_msg(500, e.__str__()))

class AddClient(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            email = request.data['email']
            store_email = Store.objects.get(email=email)
            #고객 이름, 뒷자리 가져오기
            name = request.data['name']
            last_4_digit = request.data['last_4_digit']
            check = Client.objects.filter(Q(name=name) & Q(last_4_digit=last_4_digit))
            if check.exists() : #(중복) 이미 가입된 회원
                return JsonResponse(res_msg(200, '이미 가입된 고객입니다.'))
            
            # 고객 등록하기
            client = Client.objects.create(
                name = request.POST['name'],
                last_4_digit = request.POST['last_4_digit'],
            )
         
            #고객 멤버쉽 생성
            MemberShip.objects.create(
                store = store_email,
                client_name = client
            )

            return JsonResponse(res_msg(200, '고객 등록이 완료 되었습니다.'))
        except Exception as e:
            print(e)
            return JsonResponse(res_msg(500, e.__str__()))

class GetClient(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            digit = request.data['last_4_digit']
            clients = Client.objects.filter(last_4_digit = digit)
            store_email = request.data['email']
            store = Store.objects.filter(email = store_email)
            if clients.exists() and store.exists() :
                data = []
                for client in clients:
                    membership = MemberShip.objects.filter(Q(store = store[0]) & Q( client_name = client))
                    if membership.exists():
                        data.append({'name':client.name,'stamp':membership[0].stamp})
                return JsonResponse(res_msg(200, '조회 완료',data))
            return JsonResponse(res_msg(400, '고객 정보가 없습니다.'))
        except Exception as e:
            print(e)
            return JsonResponse(res_msg(500, e.__str__()))


# 고객 도장적립 함수
# @csrf_exempt
# def membership(request) :
#     try :
#         #Get
#         if request.method == 'GET' :
#             return HttpResponse(res_msg(400, '잘못된 요청입니다.'),status=200)
#         #Post
#         elif request.method == 'POST' :
#             if # 테이블에 뒷자리가 
#             membership = Membership.objects.create(
#                 # 음 뭘 써야되지 ?_? 
#             )
#             membership.save()
#     except Exception as ex :
#         print(ex)
#         return HttpResponse(res_msg(500, '서버오류'), status=200)
