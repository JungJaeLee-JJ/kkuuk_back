from django.contrib import admin
from django.urls import path
from kkuukApp import views
from rest_framework import permissions, routers
from django.conf.urls import url
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="'꾸욱'의 API", # 타이틀
        default_version='v1', # 버전
        description="매장을 위한 쿠폰 적립 서비스 '꾸욱'입니다.", # 설명
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="cathyshim222@naver.com"),
        license=openapi.License(name="꾸욱"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,)
)


urlpatterns = [
    path(r'api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    path('admin/', admin.site.urls),
    path('api/signup', views.SignUp.as_view()),
    path('api/login',views.LogIn.as_view()),
    path('api/addclient', views.AddClient.as_view()),
    path('api/getclient', views.GetClient.as_view()),
    path('api/duplicate',views.DuplicateCheck.as_view()),
    path('api/accstamp',views.AccStamp.as_view()),
    path('api/stamphistory',views.StampHistory.as_view()),
    path('api/stamp',views.Stamp.as_view()),
    path('api/allclient',views.AllClient.as_view()),
    path('api/deleteclient',views.DeleteClient.as_view()),
    path('api/storeinfo',views.StoreInfo.as_view()),
]
