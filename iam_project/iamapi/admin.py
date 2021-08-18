from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Object)
admin.site.register(Operation)
admin.site.register(User)
admin.site.register(Permission)
admin.site.register(Role) 
admin.site.register(Permission_role)
admin.site.register(User_role)