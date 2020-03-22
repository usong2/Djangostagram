from django.contrib import admin
from .models import Dsuser

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_email', 'password')

admin.site.register(Dsuser, UserAdmin)