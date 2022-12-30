from django.contrib import admin
from .models import *


class NavElementAdmin(admin.ModelAdmin):
    list_display = ('label',)
    list_display_links = ('label',)
    search_fields = ('label',)


admin.site.register(NavElement, NavElementAdmin)
