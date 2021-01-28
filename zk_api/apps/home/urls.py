from django.urls import path

from home import views

urlpatterns = [
    path("banner/", views.BannerAPIView.as_view()),
    path("header/", views.HeaderAPIView.as_view()),
    path("footer/", views.FooterAPIView.as_view()),
]
