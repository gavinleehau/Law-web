from django.shortcuts import render
from services.models import Services
from django.core.paginator import Paginator
from home.models import whyChooseUs
from about.models import local_info
from home.models import social

# Create your views here.
def services_view(request):
	service = Services.objects.all()
	reasons = whyChooseUs.objects.all().order_by('-id')[0:3]
	info = local_info.objects.get(pk=1)
	socials = social.objects.get(pk=1)

	new_paginator = Paginator(service, per_page = 9)
	page_number = request.GET.get('page')
	page = new_paginator.get_page(page_number)

	return render(
		request = request,
		template_name = 'service.html',
		context={
			'service': service,
			'page':page,
            'new_paginator':new_paginator,
            'page_number': page_number,
			'reasons': reasons,
			'email':info.email,
			'phone':info.phoneNumber,
			'location':info.address,
			'socials': socials,
		}
	)