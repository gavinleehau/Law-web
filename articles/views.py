from django.shortcuts import render
from .models import article
from django.core.paginator import Paginator
from about.models import local_info
from home.models import social

# Create your views here.
def articles_view(request):
    articles = article.objects.all()
    info = local_info.objects.get(pk=1)

    new_paginator = Paginator(articles, per_page = 1) #sô bài mỗi page
    page_number = request.GET.get('page') 
    page = new_paginator.get_page(page_number)
    
    socials = social.objects.get(pk=1)

    return render(
        request = request,
        template_name="articles.html",
        context={
            'news':articles,
            'page':page,
            'new_paginator':new_paginator,
            'page_number': page_number,
            'email':info.email,
			'phone':info.phoneNumber,
			'location':info.address,
            'socials': socials,  
        }  
    )

def articles_detail(request, article_id):
    articles_detail = article.objects.get(id = article_id)
    info = local_info.objects.get(pk=1)
    
    return render(
        request = request,
        template_name="article_detail.html",
        context={
            'articles_detail':articles_detail,
            'email':info.email,
			'phone':info.phoneNumber,
			'location':info.address
        }  
    )