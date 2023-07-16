from django import template

register = template.Library()


@register.filter
def mediapath(object_img: str):
    return f'/static/media/product_img/{object_img}'


@register.simple_tag
def mediapath(object_img: str):
    return f'/static/media/product_img/{object_img}'
