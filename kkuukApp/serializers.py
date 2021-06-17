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