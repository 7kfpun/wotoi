# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import CustomUser, Language, Job


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user_type', 'username', 'email', 'is_staff', 'is_active',)
    list_filter = ('user_type',)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('alpha2', 'name')


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description', 'price', 'unit',
                    'until_date', 'is_approved')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Job, JobAdmin)
