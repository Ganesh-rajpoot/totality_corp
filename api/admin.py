from django.contrib import admin
from .models import UserDetails
# Register your models here.
admin.site.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = '__all__'