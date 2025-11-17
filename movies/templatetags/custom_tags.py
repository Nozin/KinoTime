from django import template
from datetime import datetime
from movies.models import Review, Movie, Author

register = template.Library()

banwords = [

]
@register.simple_tag()
def current_datetime(format_str='%b %d %Y'):
    return datetime.utcnow().strftime(format_str)

#for paginator
@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   print(d)
   for k, v in kwargs.items():
       d[k] = v
       print(d[k])
   return d.urlencode()


@register.simple_tag(takes_context=True)
def can_user_create_review(context, obj):
    request = context.get('request')

    if not request:
        return False

    user = request.user

    if not user.is_authenticated:
        return False

    if obj is None:
        return False  # объект не передан

    if not isinstance(obj, Movie):
        return False # get not movie

    try:
        author = user.author
    except ObjectDoesNotExist:
        return False # user is not author

    return not Review.objects.filter(movie=obj, author=author).exists()

