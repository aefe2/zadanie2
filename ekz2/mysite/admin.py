from django.contrib import admin

from ekz2.mysite.models import Services, User

# Register your models here.
admin.site.register(User)
admin.site.register(Services)