from django.urls import path

from course import views
urlpatterns =[
    path("category/", views.CourseCategoryAPIVIew.as_view()),
    path("list/", views.CourseAPIView.as_view()),
    path("detail/<str:id>/", views.CourseAPIView1.as_view()),
    path("chapter/", views.CourseLessonAPIView1.as_view()),
]