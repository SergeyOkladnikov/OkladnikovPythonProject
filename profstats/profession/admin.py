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


class NonProfConnectedGraphAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_shown')
    list_editable = ('is_shown',)
    list_display_links = ('name',)
    search_fields = ('name',)


class ProfConnectedGraphAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_shown', 'profession')
    list_editable = ('is_shown',)
    list_display_links = ('name',)
    search_fields = ('name',)


class ComparisonGraphAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_shown', 'profession')
    list_editable = ('is_shown',)
    list_display_links = ('name',)
    search_fields = ('name',)


class PageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


class NonProfConnectedTableDataAdmin(admin.ModelAdmin):
    list_display = ('label', 'is_shown')
    list_editable = ('is_shown',)
    list_display_links = ('label',)
    search_fields = ('label',)


class ProfConnectedTableDataAdmin(admin.ModelAdmin):
    list_display = ('label', 'is_shown')
    list_editable = ('is_shown',)
    list_display_links = ('label',)
    search_fields = ('label',)


admin.site.register(NavElement, NavElementAdmin)
admin.site.register(FooterElement, FooterElementAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(NonProfConnectedGraph, NonProfConnectedGraphAdmin)
admin.site.register(ProfConnectedGraph, ProfConnectedGraphAdmin)
admin.site.register(ComparisonGraph, ComparisonGraphAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(NonProfConnectedTableData, NonProfConnectedTableDataAdmin)
admin.site.register(ProfConnectedTableData, ProfConnectedTableDataAdmin)
