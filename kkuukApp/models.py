from django.db import models
#모델명 함부로 바꾸지 말기

class Store(models.Model):
    id = models.AutoField(primary_key=True) #업체별 고유번호 AutoField로 지정하면 번호가 순차적으로 자동 부여된다
    email = models.EmailField(max_length=255)
<<<<<<< HEAD
    call = models.CharField(null=True, max_length=20)
    name = models.CharField(null=True, max_length=255)
    pwd = models.CharField(null=True, max_length=12)
=======
    call = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    pwd = models.CharField(max_length=12)
>>>>>>> 695432cf6d35981816f332053e6f5381c1a31152
    created_at = models.DateTimeField(auto_now_add=True) #날짜와 시간을 갖는 필드
    is_deleted = models.BooleanField(default=False) #데이터 관리할 때 false로 기본값
    # objects = UserManager()

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True, max_length=255)
    last_4_digit = models.CharField(null=True, max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    # store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_name')
    
class Histroy(models.Model):
    id = models.AutoField(primary_key=True)
    trade_type_choices = (
        ('save','적립'),
        ('use','사용'),
    )
    trade_type = models.CharField(
        max_length=5,
        choices=trade_type_choices,
        null=True,
    )
<<<<<<< HEAD
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
=======
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='user')
>>>>>>> 695432cf6d35981816f332053e6f5381c1a31152
    trade_at = models.DateTimeField(auto_now_add=True)
    before_stamp = models.IntegerField(default=0)
    val_stamp = models.IntegerField(default=0)
    after_stamp = models.IntegerField(default=0)


class MemberShip(models.Model):
<<<<<<< HEAD
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
=======
    seller = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='seller')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client')
>>>>>>> 695432cf6d35981816f332053e6f5381c1a31152
    stamp = models.IntegerField(default=0)