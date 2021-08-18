from rest_framework import serializers
from kkuukApp.models import Store,Client,Histroy,MemberShip

# class StoreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Store
#         fields = ['email','call','username','password']
    
# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = ['name','last_4_digit']

# class HistroySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Histroy
#         fields = ['name','last_4_digit']

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True, max_length=255)
    last_4_digit = models.CharField(null=True, max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)