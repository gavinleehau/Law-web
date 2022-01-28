from django.shortcuts import render
from .models import Questions, social, whyChooseUs
from about.models import local_info, member
from services.models import Services
from articles.models import article


# Create your views here.
def index(request):
  questions = Questions.objects.all().order_by('-id')[0:5]
  services = Services.objects.all().order_by('-id')[0:3]
  reasons = whyChooseUs.objects.all().order_by('-id')[0:3]
  socials = social.objects.get(pk=1)
  info_lawyers = member.objects.all().order_by('-id')[0:4]
  info = local_info.objects.get(pk=1)
  articles = article.objects.all()

  return render(
    request=request,
    template_name="index.html",
    context = {
      'questions': questions,
      'socials': socials,
      'services': services,
      'reasons': reasons,
      'descriptions': info.descriptions,
      'info_lawyers': info_lawyers,
      'articles': articles,
      'email':info.email,
			'phone':info.phoneNumber,
			'location':info.address
    }
  )

