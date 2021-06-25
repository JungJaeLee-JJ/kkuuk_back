from .models import Store, Client, MemberShip, Histroy
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
            email = request.data['email']
            password = request.data['password']
            stores = Store.objects.filter(email=email)
            if not stores.exists():
                return JsonResponse(res_msg(400, '등록되지 않은 email 입니다.'))
            store = stores[0]
            data = {'username':store.username,'email':email,'password':password}
            serializer = AuthTokenSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            token, _ = Token.objects.get_or_create(user=store)
            return JsonResponse(res_msg(200, '로그인에 성공하였습니다.',{'token':token.key,'email':email,'call':store.call,'username':store.username}))
        except Exception as e:
            print(e)
            return JsonResponse(res_msg(500, e.__str__()))

class AddClient(APIView):
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema(request_body=AddClientSerializer)
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
                    membership = MemberShip.objects.filter(Q(store = store[0]) & Q( client_digit = client))
                    if membership.exists():
                        data.append({'name':client.name,'stamp':membership[0].stamp})
                return JsonResponse(res_msg(200, '조회 완료',data))
            return JsonResponse(res_msg(400, '고객 정보가 없습니다.'))
        except Exception as e:
            print(e)
            return JsonResponse(res_msg(500, e.__str__()))

class AccStamp(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            email = request.data['email']
            digit = request.data['last_4_digit']
            name = request.data['name']
            val = int(request.data['val'])

            # 가게 조회
            stores = Store.objects.filter(email=email)
            if not stores.exists():
                return JsonResponse(res_msg(400, '등록되지 않은 email 입니다.'))
            store = stores[0]
            
            # 고객 조회
            clients = Client.objects.filter(Q(last_4_digit=digit)&Q(name=name))
            if not clients.exists():
                return JsonResponse(res_msg(400, '등록되지 않은 고객입니다.'))
            client = clients[0]

            # 멤버쉽 조회
            memberships = MemberShip.objects.filter(Q(store=store)&Q(client_name=client))
            if not memberships.exists():
                return JsonResponse(res_msg(400, '등록되지 않은 멤버 입니다.'))
            membership = memberships[0]

            # 히스토리 저장
            trade_type = 'save' if val > 0 else 'use'
            Histroy.objects.create(
                trade_type = trade_type,
                user = client,
                store = store,
                before_stamp = membership.stamp,
                val_stamp = val,
                after_stamp = membership.stamp + val
            )

            # 값 저장
            membership.stamp = membership.stamp + val
            membership.save()

            return JsonResponse(res_msg(200, '성공',{'stamp':membership.stamp}, {'client':client.name}))

        except Exception as e:
            print(e)
            return JsonResponse(res_msg(500, e.__str__()))

# 스탬프 적립, 사용 내역 조회 함수
class StampHistory(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            email = request.data['email']
            digit = request.data['last_4_digit']
            name = request.data['name']

            # 가게 조회
            stores = Store.objects.filter(email=email)
            if not stores.exists():
                return JsonResponse(res_msg(400, '등록되지 않은 email 입니다.'))
            store = stores[0]

            # 고객 조회
            clients = Client.objects.filter(Q(last_4_digit=digit)&Q(name=name))
            if not clients.exists():
                return JsonResponse(res_msg(400, '등록되지 않은 고객입니다.'))
            client = clients[0]

            # 히스토리 조회
            history = Histroy.objects.filter(Q(store=store)&Q(user=client))
            if not history.exists():
                return JsonResponse(res_msg(400, '적립 또는 사용 내역이 없습니다'))
            for h in history :
                data = []
                data.append({'날짜':h.trade_at, '이전 스탬프 개수':h.befor_stamp, '적립/사용 개수':h.val_stamp, '현재 스탬프 개수':h.after_stamp})
            return JsonResponse(res_msg(200, '조회 완료',data))
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
