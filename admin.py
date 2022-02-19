from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Pidrov)

# @admin.register(Pidrov)
# class PidrovAdmin(admin.ModelAdmin):
#     list_display = ['pk', 'name', 'tema']
#     # list_editable = ['tema']
#     list_filter = ['name', 'tema']
#     list_display_links = ['name']
