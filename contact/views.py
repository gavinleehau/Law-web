from django.shortcuts import render
from .models import contact
from about.models import local_info
from django.utils.decorators import method_decorator
from home.models import social

# Create your views here.
def contact_view(request):
	data = contact()
	if request.method == 'POST':
		data.email = request.POST['email']
		data.name = request.POST['name']
		data.phone = request.POST['phone']
		data.subject = request.POST['subject']
		data.message = request.POST['message']
		data.save()

	info = local_info.objects.get(pk=1)
	socials = social.objects.get(pk=1)

	return render(
		request = request,
		template_name="contact.html",
		context = {
			'email':info.email,
			'phone':info.phoneNumber,
			'location':info.address,
			'socials': socials,
		}
	)
  	