from django.contrib import admin
from .models import local_info, member, history

# Register your models here.

admin.site.register(local_info)
admin.site.register(member)
admin.site.register(history)