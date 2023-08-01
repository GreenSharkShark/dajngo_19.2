from django import template

register = template.Library()


@register.filter
def mediapath(object_img: str):
    return f'/media/{object_img}'


@register.simple_tag
def mediapath(object_img: str):
    return f'/media/{object_img}'
