from django import template
import re
import string

register = template.Library()

banwords = ['взрывная', 'политическая']
@register.filter()
def review_censor(text):
    if type(text) != str:
        raise TypeError
    # Разбить текст на слова и знаки препинания
    # \w+ — одно или несколько букв/цифр (слова)
    # | — или
    # [^\w\s] — один символ, который не буква и не пробел (например, запятая, точка, восклицательный знак)
    tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
    result = []
    for token in tokens:
        clean = token.lower().strip(string.punctuation)
        if clean in banwords:
            pass
            result.append(f'''{token[0]}{'*' * (len(token)-1)}''')
        else:
            pass
            result.append(token)
    output = ' '.join(result)
    # шаблон ищет один или несколько пробелов s+, за которыми сразу идёт запятая, точка, восклицательный знак и т.д ([,.!?;:]).
    output = re.sub(r'\s+([,.!?;:])', r'\1', output)
    return output


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()









