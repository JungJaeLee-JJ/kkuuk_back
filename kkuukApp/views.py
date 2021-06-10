from .models import Store
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

#response 메세지
def res_msg(code, msg) :
    print(code,msg)
    return json.dumps({'code':code, 'msg':msg},ensure_ascii=False)

@csrf_exempt
def Signup(request):
    try :
        if request.method == 'GET':
            return HttpResponse(res_msg(400, '잘못된 요청입니다.'),status=200)
        elif request.method == 'POST':
            store = Store.objects.create(
            email = request.POST['email'],
            call = request.POST['call'],
            store_name = request.POST['name'],
            pwd = request.POST['pwd'],
        )
        store.save()
        return HttpResponse(res_msg(200,'회원가입이 완료되었습니다.'), status=200)
    except Exception as ex :
        print(ex)
        return HttpResponse(res_msg(500, '서버오류'), status=200)

@csrf_exempt
# 로그인 함수
def Login(request):
    try :
        #GET
        if request.method == 'GET':
            return HttpResponse(res_msg(400, '잘못된 요청입니다.'),status=200)
        #POST
        elif request.method == 'POST':
            email = request.POST['email']
            pwd = request.POST['pwd']
            store = Store.objects.get(email=email)
            if store.pwd == pwd :
                return HttpResponse(res_msg('200', '로그인 되었습니다.'), status=200)
            return HttpResponse(res_msg(400, '비밀번호가 다릅니다.'), status=200)
    except Exception as ex:
        print(ex)
        return HttpResponse(res_msg(500, '서버오류'), status=200)
