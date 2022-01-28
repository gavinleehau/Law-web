from django.shortcuts import render
from .models import history, local_info, member
from about.models import local_info
from home.models import social

# Create your views here.
def about_view(request):
	histories = history.objects.all()
	info = local_info.objects.get(pk=1)
	info_lawyers = member.objects.all().order_by('-id')[0:4]
	socials = social.objects.get(pk=1)
	
	return render (
		request=request,
		template_name="about.html",
		context = {
			'histories': histories,
			'descriptions': info.descriptions,
			'info_lawyers': info_lawyers,
			'email':info.email,
			'phone':info.phoneNumber,
			'location':info.address,
			'socials': socials,
		}
	)

def history_data(request, history_id):
	history_data = history.objects.get(id = history_id)
	return render (
		request=request,
		template_name="about.html",
		context = {
			'history_data': history_data
		}
	)