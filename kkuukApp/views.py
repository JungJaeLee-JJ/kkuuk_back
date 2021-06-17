from .models import MemberShip, Store, Client
from django.http import HttpResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import json

#response 메세지
def res_msg(code, msg) :
    print(code,msg)
    return json.dumps({'code':code, 'msg':msg},ensure_ascii=False)

# 매장 등록 함수
@csrf_exempt
def signup(request):
    try :
        if request.method == 'GET' :
            return HttpResponse(res_msg(400, '잘못된 요청입니다.'),status=200)
        elif request.method == 'POST' :
            store = Store.objects.create(
                email = request.POST['email'],
                call = request.POST['call'],
                name = request.POST['name'],
                pwd = request.POST['pwd'],
        )
        # store.save()
        return HttpResponse(res_msg(200,'회원가입이 완료되었습니다.'), status=200)
    except Exception as ex :
        print(ex)
        return HttpResponse(res_msg(500, '서버오류'), status=200)

# 로그인 함수
@csrf_exempt
def login(request):
    try :
        #GET
        if request.method == 'GET' :
            return HttpResponse(res_msg(400, '잘못된 요청입니다.'),status=200)
        #POST
        elif request.method == 'POST' :
            email = request.POST['email']
            pwd = request.POST['pwd']
            store = Store.objects.get(email=email)
            if store.pwd == pwd :
                return HttpResponse(res_msg('200', '로그인 되었습니다.'), status=200)
            return HttpResponse(res_msg(400, '비밀번호가 다릅니다.'), status=200)
    except Exception as ex:
        print(ex)
        return HttpResponse(res_msg(500, '서버오류'), status=200)

#고객 등록 함수
@csrf_exempt
def addClient(request):
    try :
        #Get
        if request.method == 'GET' :
            return HttpResponse(res_msg(400, '잘못된 요청입니다.'),status=200)
        #POST
        elif request.method == 'POST' :
            #가게 이메일 가져오기
            email = request.POST['email']
            store = Store.objects.get(email=email)
            #고객 이름, 뒷자리 가져오기
            name = request.POST['name']
            last_4_digit = request.POST['last_4_digit']
            check = Client.objects.filter(Q(name=name) & Q(last_4_digit=last_4_digit))
            if check.exists() : #(중복) 이미 가입된 회원
                return HttpResponse(res_msg('200', '이미 가입된 고객입니다.'), status=200)
            # 고객 등록하기
            client = Client.objects.create(
            name = request.POST['name'],
            last_4_digit = request.POST['last_4_digit'],
            )
            # client.save()
            #고객 멤버쉽 생성
            membership = MemberShip.objects.create(
                store = store,
                client_name = client
            )
            # membership.save()
            return HttpResponse(res_msg(200, '고객 등록이 완료 되었습니다.'), status=200)
    except Exception as ex :
        print(ex)
        return HttpResponse(res_msg(500, '서버오류'), status=200)

# 고객 조회 함수
# @csrf_exempt
# def getClient(request) :
#     try :
#         #Get
#         if request.method == 'GET' :
#             return HttpResponse(res_msg(400, '잘못된 요청입니다.'),status=200)
#         #POST
#         elif request.method == 'POST' :
#             digit = request.POST['last_4_digit']
#             check = Client.objects.filter(last_4_digit = digit)
#             #고객 조회에 매장 아이디도 조회하기
#             if check #조건 몰라서 못씀.. : # 뒷자리가 고객 정보에 있다면
#                 membership = MemberShip.objects.create(
#                     #멤버십 생성하기
#                     store = request.POST['store'],
#                     client_name = request.POST['client_name'],
#                     stamp = request.POST['stamp'],
#                 )
#                 membership.save()
#                 return HttpResponse(res_msg(200, '적립되었습니다.'), status=200)
#             else : #뒷자리가 고객 정보에 없다면
#                 # 고객 등록하기
#                 client = Client.objects.create(
#                 name = request.POST['name'],
#                 last_4_digit = request.POST['last_4_digit'],
#                 )
#                 client.save()
#                 return HttpResponse(res_msg(200, '고객이 등록되었습니다.'),status=200)
#     except Exception as ex :
#         print(ex)
#         return HttpResponse(res_msg(500, '서버오류'), status=200)


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
