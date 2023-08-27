from django import template
from catalog.models import *

register = template.Library()

@register.simple_tag()
def mediapath(image_path):
    return '/media/' + str(image_path)


