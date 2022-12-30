from django import template
from profession.models import *

register = template.Library()


@register.inclusion_tag('profession/nav-elements.html')
def show_nav():
    nav_elements = NavElement.objects.all()
    return {"nav_elements": nav_elements}
