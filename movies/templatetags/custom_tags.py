from django import template
from datetime import datetime

register = template.Library()

banwords = [

]
@register.simple_tag()
def current_datetime(format_str='%b %d %Y'):
    return datetime.utcnow().strftime(format_str)

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   print(d)
   for k, v in kwargs.items():
       d[k] = v
       print(d[k])
   return d.urlencode()