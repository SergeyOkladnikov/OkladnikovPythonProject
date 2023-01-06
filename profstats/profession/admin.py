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

    fieldsets = (
        ('Общая информация', {
            'fields': ('name',
                       'text_block_1',
                       'image_1',
                       'image_1_caption',
                       'text_block_2',
                       'image_2',
                       'image_2_caption',
                       'text_block_3',
                       'image_3',
                       'image_3_caption')
        }),
        ('Востребованность', {
            'fields': ('years_stats',
                       'years_salary_graph',
                       'years_vac_num_graph',
                       'years_salary_for_prof_graph',
                       'years_vac_num_for_prof_graph',
                       'years_salary_comparison_graph',
                       'years_vac_num_comparison_graph')
        }),
        ('География', {
            'fields': ('areas_stats',
                       'areas_salary_graph',
                       'areas_vac_fractions_graph')

        }),
        ('Навыки', {
            'fields': ('skills_stats',
                       'top_skills_total_graph')
        })
    )


admin.site.register(NavElement, NavElementAdmin)
admin.site.register(FooterElement, FooterElementAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Profession, ProfessionAdmin)
