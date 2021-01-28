from django.shortcuts import render
from django_redis import get_redis_connection
# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from course.models import Course
from zk_api.settings.constants import IMG_SRC


class CartViewSet(ViewSet):
    """购物车视图"""

    #只有登录且认证成功的用户才可以访问
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def add_cart(self,request):
        """
        将课程添加到购物车
        :param request: 用户id 课程id 勾选状态  有效期
        :return:
        """
        course_id=request.data.get("course_id")
        #当前视图只允许认证后的用户访问
        #如果登录成功会把用户的信息解析到request模块user中
        user_id=request.user.id
        #是否勾选 默认为ture
        select=True
        #有效期  默认为永久
        expire=0


        #校验前端传来的数据
        try:
          Course.objects.filter(is_show=True, is_delete=False,pk=course_id)

        except Course.DoesNotExist:
            return Response({"message":"参数有误，不存在"},status=status.HTTP_400_BAD_REQUEST)


        try:
            redis_connection = get_redis_connection("cart")
            #多次操作redis时建议使用管道
            pipeline=redis_connection.pipeline()
            #开启管道
            pipeline.multi()
            #保存商品的信息以及对应的有效期  hash
            pipeline.hset("cart_%s"% user_id,course_id,expire)

            #保存商品的勾选状态  set
            pipeline.sadd("select_%s"%user_id,course_id)

            #执行管道
            pipeline.execute()
            #获取购物车中的商品数量
            cart_len=redis_connection.hlen("cart_%s"% user_id)
        except:
            return Response({"message":"参数有误，添加购物车失败"},status=status.HTTP_400_BAD_REQUEST)

        return Response({"message":"添加购物车成功",

                         "cart_length":cart_len})


    def list_cart(self,request):
        """展示购物车"""
        user_id=request.user.id
        redis_connection = get_redis_connection("cart")
        cart_list_byte=redis_connection.hgetall("cart_%s"% user_id)
        select_list_byte=redis_connection.smembers("select_%s"%user_id)


        # 循环从MySQL中获取课程信息

        data=[]

        for course_id_byte, expire_id_byte in cart_list_byte.items():
            course_id=int(course_id_byte)
            expire_id=int(expire_id_byte)

            try:
                course=Course.objects.get(is_show=True, is_delete=False, pk=course_id)

            except Course.DoesNotExist:
                continue
                #将购物车所需信息返回
            data.append({
                    #勾选状态
                "selected":True if course_id_byte in select_list_byte else False,
                "course_img": IMG_SRC+ course.course_img.url,
                "name":course.name,
                "id":course.id,
                "expire_id":expire_id,
                "price":course.price,

                })
        return Response(data)

class CartChangeViewSet(ViewSet):
    #登录用户才可以进入
    #只有登录且认证成功的用户才可以访问
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def change_cart(self,request):

        course_id=request.data.get("course_id")
        #当前视图只允许认证后的用户访问
        #如果登录成功会把用户的信息解析到request模块user中
        user_id=request.user.id
        #是否勾选 默认为ture
        select=request.data.get("select")
        #有效期  默认为永久
        expire=0

        redis_connection = get_redis_connection("cart")
        try:
            if select:
                redis_connection.sadd("selected_%s"%user_id,course_id)
            else:
                redis_connection.srem("selected_%s" % user_id, course_id)

        except:
            return Response({"message": "参数有误，不存在"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "添加购物车成功",

                        })

class CartDelViewSet(ViewSet):
        # 登录用户才可以进入
        # 只有登录且认证成功的用户才可以访问
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def delete_cart(self, request):
        course_id = request.data.get("course_id")
        user_id = request.user.id
        redis_connection = get_redis_connection("cart")
        redis_connection.srem("selected_%s" % user_id, course_id)
        redis_connection.hdel("cart_%s" % user_id, course_id)

        return Response({"msg": "删除成功"})




