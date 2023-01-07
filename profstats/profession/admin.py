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


class HeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_logo_changed', 'is_logo_shown', 'is_prof_name_shown', 'is_chosen')
    list_editable = ('is_logo_changed', 'is_logo_shown', 'is_prof_name_shown', 'is_chosen')
    list_display_links = ('name',)
    search_fields = ('name',)


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_chosen')
    list_editable = ('is_chosen',)
    list_display_links = ('name',)
    search_fields = ('name',)


class DemandOneVarGraphAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_shown')
    list_editable = ('is_shown',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(NavElement, NavElementAdmin)
admin.site.register(FooterElement, FooterElementAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(DemandOneVarGraph, DemandOneVarGraphAdmin)
