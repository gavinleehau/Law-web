from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.articles_view, name="articles"),
    url(r"^articles_detail/(?P<article_id>[0-9]+)$",views.articles_detail, name="articles_detail"),
]