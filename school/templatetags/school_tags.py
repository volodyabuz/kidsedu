from django import template
from school.models import *

register = template.Library()

@register.simple_tag(name='getphoto')
def get_photoedu():
    return PhotoEducations.objects.all()

@register.inclusion_tag('school/list_progs.html')
def c_list(filter=None):
    if filter:
        clist = PhotoEducations.objects.filter(pk__lte=filter)
    else:
        clist = PhotoEducations.objects.all()
    return {"clist": clist}
