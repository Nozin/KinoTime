from django import template
from datetime import datetime

register = template.Library()

banwords = [

]
@register.simple_tag()
def current_datetime(format_str='%b %d %Y'):
    return datetime.utcnow().strftime(format_str)