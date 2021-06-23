"""kkuuk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from kkuukApp import views
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
# from drf_yasg import openapi
# from django.urls import path, include
# from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

# schema_view = get_swagger_view(title="My API")

# schema_url_v1_patterns = [
#     url(r'^v1/', include('kkuuk.urls', namespace='kkuuk_api')),
# ]
 
# schema_view_v1 = get_schema_view(
#     openapi.Info(
#         title="KKUUK Open API",
#         default_version='v1',
#         description="안녕하세요. 꾸욱의 Open API 문서 페이지 입니다.",
#         terms_of_service="https://www.google.com/policies/terms/",
#     ),
#     validators=['flex'], #'ssv'],
#     public=True,
#     permission_classes=(AllowAny,),
#     patterns=schema_url_v1_patterns,
# )
 
urlpatterns = [
    url('api/docs', schema_view),
    # url(r'^admin/', admin.site.urls),
    # url(r'^v1/', include('kkuuk.urls', namespace='kkuuk_api')),
 
    # # Auto DRF API docs
    # url(r'^swagger(?P<format>\.json|\.yaml)/v1$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    # url(r'^swagger/v1/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # url(r'^redoc/v1/$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    path('admin/', admin.site.urls),
    path('api/signup', views.SignUp.as_view()),
    path('api/login',views.LogIn.as_view()),
    path('api/addclient', views.AddClient.as_view()),
    path('api/getclient', views.GetClient.as_view()),
    path('api/duplicate',views.DuplicateCheck.as_view()),
    path('api/accstamp',views.AccStamp.as_view()),
]
