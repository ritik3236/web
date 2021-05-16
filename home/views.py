from django.shortcuts import render

from home.models import *


def sort_by_values(dic: {}):
    return {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}


# Create your views here.
def home(request, *args, **kwargs):
    context = {}
    for obj in Course.objects.all().iterator():
        context.update({str(obj.id): obj.c_name})
    return render(request, 'home/home.html', {'context': sort_by_values(context).items()})


def bsc(request, *args, **kwargs):
    print(request.GET)
    return render(request, 'home/home.html')
