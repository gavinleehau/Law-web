from django.shortcuts import render
from .models import news 
from django.core.paginator import Paginator
from about.models import local_info
from home.models import social

# Create your views here.
def news_view(request):
    new = news.objects.all()
    info = local_info.objects.get(pk=1)

    new_paginator = Paginator(new, per_page = 5) #sô bài mỗi page
    page_number = request.GET.get('page') 
    page = new_paginator.get_page(page_number)
    socials = social.objects.get(pk=1)

    return render(
        request = request,
        template_name="news.html",
        context={
            'news':new,
            'page':page,
            'new_paginator':new_paginator,
            'page_number': page_number,
            'email':info.email,
			'phone':info.phoneNumber,
			'location':info.address,
            'socials': socials,
        }  
    )

def news_detail(request, news_id):
    news_detail = news.objects.get(id = news_id)
    info = local_info.objects.get(pk=1)

    return render(
        request = request,
        template_name="news_detail.html",
        context={
            'news_detail':news_detail,
            'email':info.email,
			'phone':info.phoneNumber,
			'location':info.address
        }  
    )