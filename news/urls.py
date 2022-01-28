from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.news_view, name="news"),
    url(r"^news_detail/(?P<news_id>[0-9]+)$",views.news_detail, name="news_detail"),
]