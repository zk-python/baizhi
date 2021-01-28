from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from course.models import CourseCategory, Course, CourseChapter
from course.pagination import CoursePageNumberPagination
from course.serializer import CourseCategoryModelSerializer, CourseModelSerializer, ListModelSerializer, \
    CourseChapterModelSerializer


class CourseCategoryAPIVIew(ListAPIView):
    """课程分类信息查询"""
    queryset = CourseCategory.objects.filter(is_show=True, is_delete=False).order_by("-orders")
    serializer_class = CourseCategoryModelSerializer


class CourseAPIView(ListAPIView):
    """课程信息查询"""
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseModelSerializer

    # 分类查询的模板类
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ("course_category",)

    # 排序
    ordering_fields = ("id", "students", "price")

    # 分页
    pagination_class = CoursePageNumberPagination


class CourseAPIView1(RetrieveAPIView):
    """课程详细信息展示"""
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = ListModelSerializer
    lookup_field = "id"

class CourseLessonAPIView1(ListAPIView):
    """课程章节与课时信息"""
    queryset = CourseChapter.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseChapterModelSerializer
    lookup_field = "id"

    filter_backends = [DjangoFilterBackend]
    #章节与课程的外键
    filter_fields = ["course"]
