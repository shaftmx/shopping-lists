## tags.py http://gnuvince.wordpress.com/2007/09/14/a-django-template-tag-for-the-current-active-page/

from django import template

register = template.Library()

@register.simple_tag
def active(request, pattern):
    import re
    try:
        if re.search(pattern, request.path):
            return 'active'
        return ''
    except:
        return ''

@register.simple_tag
def itemsless(myobject):
    count = 0
    try:
        items = myobject.items.all()
    except:
        # Full list, only items
        items = myobject
    for item in items:
        if item.outOfStock:
            count += 1
    return count

@register.simple_tag
def countbadgetype(myobject):
    count = 0
    total = 0
    try:
        items = myobject.items.all()
    except:
        # Full list, only items
        items = myobject
    for item in items:
        if item.outOfStock:
            count += 1
        total +=1
    if count == 0:
        return 'badge-success'
    elif count <= total/2:
        return 'badge-warning'
    else:
        return 'badge-danger'
