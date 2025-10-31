from django import template

register = template.Library()

banwords = [

]

def review_censor(value):

    return value