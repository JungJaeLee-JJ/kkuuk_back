from django.db import models
from django.contrib.auth.models import User
#모델명 함부로 바꾸지 말기

class Store(User):
    # id = models.AutoField(primary_key=True) #업체별 고유번호 AutoField로 지정하면 번호가 순차적으로 자동 부여된다
    # email = models.EmailField(max_length=255)
    call = models.CharField(max_length=20)
    # name = models.CharField(max_length=255)
    # pwd = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True) #날짜와 시간을 갖는 필드
    is_deleted = models.BooleanField(default=False) #데이터 관리할 때 false로 기본값
    # objects = UserManager()
    def __str__(self):
        return self.username

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
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='user')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store')
    trade_at = models.DateTimeField(auto_now_add=True)
    before_stamp = models.IntegerField(default=0)
    val_stamp = models.IntegerField(default=0)
    after_stamp = models.IntegerField(default=0)


class MemberShip(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    stamp = models.IntegerField(default=0)