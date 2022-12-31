from django.contrib import admin
from .models import *


class NavElementAdmin(admin.ModelAdmin):
    list_display = ('label',)
    list_display_links = ('label',)
    search_fields = ('label',)


class FooterElementAdmin(admin.ModelAdmin):
    list_display = ('label', 'content')
    list_display_links = ('label', 'content')
    search_fields = ('label',)


admin.site.register(NavElement, NavElementAdmin)
admin.site.register(FooterElement, FooterElementAdmin)
