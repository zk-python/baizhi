from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from home.models import Banner, Nav
from home.serializer import BannerModelSerializer, HeaderModelSerializer


class BannerAPIView(ListAPIView):
    """轮播图接口"""
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by("-orders")
    serializer_class = BannerModelSerializer



class HeaderAPIView(ListAPIView):
    """头导航栏入口"""
    queryset = Nav.objects.filter(is_show=True,position=1, is_delete=False).order_by("-orders")
    serializer_class = HeaderModelSerializer


class FooterAPIView(ListAPIView):
    """脚导航栏入口"""
    queryset = Nav.objects.filter(is_show=True,position=2, is_delete=False).order_by("-orders")
    serializer_class = HeaderModelSerializer



