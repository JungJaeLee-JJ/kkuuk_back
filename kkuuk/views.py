from .models import Store
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password


@csrf_exempt
def signup(request):
    try:
        store = Store.objects.create(
            email = request.POST['email'],
            call = request.POST['call'],
            store_name = request.POST['name'],
            pwd = request.POST['pwd'],
        )
        store.save()
        return HttpResponse('성공', status=200)
    except:
        return HttpResponse('실패', status=400)

@csrf_exempt
# 로그인 함수
def login(request):

    # GET 방식 요청 -> 로그인 페이지 요청 
    if request.method == 'GET':
        ret = {'errorCode':400, 'msg':'잘못된 요청입니다.'}
        return HttpResponse(ret,status=400)
    return HttpResponse('실패',status=400)
    
	
    # # POST 방식 요청 -> 사용자가 보내는 데이터와 데이터베이스의 정보 일치여부 확인 
    # elif request.method == 'POST':
    #     username = request.POST.get('email',None)
    #     password = request.POST.get('pwd',None)
		
    #     # 응답 데이터
    #     res_data = {}
        
    #     # 모든 필드를 채우지 않았을 경우
    #     if not (email and pwd):
    #         res_data['error'] = '이메일과 비밀번호를 모두 입력하세요.'
        
    #     # 모든 필드를 채웠을 경우
    #     else:
     
    #         # 사용자가 보낸 username을 가지고 있는 데이터를 가져온다.
    #         # 일치하는 데이터가 없을 때 예외처리 (get_object_or_404) 
    #         user = User.objects.get(username=username)
            
    #         # 사용자가 보낸 password와 데이터베이스에 저장된 password 일치 여부 확인 
    #         # check_password 로 hash화 되어있는 비밀번호를 대조하기
    #         if check_password(password, user.password):
                
    #             # 비밀번호가 일치하면 session을 사용해 user.id 를 넘겨준다.
    #             request.session['user'] = user.id
                
    #             # 로그인 성공 후 127.0.0.1:8000/ 이동   
    #             return redirect('/')
            
    #         # 비밀번호가 일치하지 않으면 에러
    #         else:
    #             res_data['error'] = '비밀번호가 일치하지 않습니다'
		
    #     # 로그인 실패 및 오류메세지와 함께 응답
    #     return render(request, 'login.html', res_data)

# 127.0.0.1:8000/ 
def home(request):

    # login을 통해서 확인된 user는 session을 통해 user.id를 넘겨 받았다.
    user_id = request.session.get('user')
    
    # user_id유무를 통해 login판단
    if user_id:
        user = User.objects.get(pk=user_id)
        return HttpResponse(f'{user} login success')
	
    return HttpResponse('Home')
    
# 로그아웃 함수    
def logout(request):
	
    # 로그아웃은 session에 저장된 user_id값을 지우면 된다.
    if request.session.get('user'):
        del(request.session['user'])
	
    # 로그아웃 후 127.0.0.1:8000/ 이동   
    return redirect('/')
        

# # 매장 목록 및 새 매장 등록
# class StoreListAPIView(APIView):
#     def get(self, request):
#         serializer = StoreSerializer(Store.objects.all(), many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = StoreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)  
      
# # 매장 내용, 수정, 삭제
# class PostDetailAPIView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Store, pk=pk)
      
#     def get(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = StoreSerializer(post)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#       	post = self.get_object(pk)
#         serializer = StoreSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)