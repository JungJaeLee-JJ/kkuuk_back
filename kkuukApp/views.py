from .models import Store
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Signup(request):
    store = Store.objects.create(
        email = request.POST['email'],
        call = request.POST['call'],
        store_name = request.POST['name'],
        pwd = request.POST['pwd'],
    )
    store.save()
    return HttpResponse('성공', status=200)