from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from user import views

urlpatterns = [
    # 借助于jwt完成登录请求
    path("login/", obtain_jwt_token),
    #极验
    path("captcha/", views.CaptchaAPIView.as_view()),
    #注册逻辑
    path("users/", views.UserAPIView.as_view()),
    #发送短信
    path("message/", views.MessageAPIView.as_view()),
    #获取手机号
    path("phones/", views.PhoneAPIView.as_view()),

]
