from django import template

register = template.Library()

banwords = [

]
@register.filter()
def review_censor(value):

    return value