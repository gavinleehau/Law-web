"""mysite URL Configuration

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
from django.conf.urls import include
from home import views as home_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_views.index ),
    path('admin/', admin.site.urls),
    path('home/', include("home.urls")),
    path('about/',include("about.urls")),
    path('services/', include("services.urls")),
    path('articles/', include("articles.urls")),
    path('news/', include("news.urls")),
    path('contact/', include("contact.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
