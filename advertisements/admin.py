from django.contrib import admin

from advertisements.models import Adv


@admin.register(Adv)
class AdvRouter(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'open']
