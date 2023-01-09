from django import template
from profession.models import *

register = template.Library()


@register.inclusion_tag('profession/nav-elements.html')
def render_nav():
    nav_elements = NavElement.objects.all()
    return {"nav_elements": nav_elements}


@register.inclusion_tag('profession/footer-elements.html')
def render_footer():
    footer_elements = FooterElement.objects.all()
    return {"footer_elements": footer_elements}


@register.inclusion_tag('profession/header.html')
def render_header():
    from profession.views import profession
    if Header.objects.filter(is_chosen=True):
        header = Header.objects.filter(is_chosen=True)[0]
    else:
        header = None
    return {'header': header, 'prof_name': profession.name if profession else None}


@register.filter
def format_date_string(value):
    return f'{value[8:10]}.{value[5:7]}.{value[0:4]}'
