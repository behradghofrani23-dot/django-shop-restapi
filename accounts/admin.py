from django.contrib import admin
from .models import CustomUser
# Register your models here.
admin.site.register(CustomUser)
class ContactAdmin(admin.ModelAdmin):
    list_display=['username','first_name']