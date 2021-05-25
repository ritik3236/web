from django.http import JsonResponse
from django.core import serializers
from api.models import *
import random
# Create your views here.


def quote_record(request):
    lst = []
    image_url = []
    q = QuotesApi.objects.all()
    for i in q:
        lst.append(i)
    rq  = random.sample(lst, 4)
    for i in rq:
        try:
            image_url.append(i.author_img.url)
        except Exception as e:
            image_url.append('img not found')
    randomized_quote = serializers.serialize('json', rq)
    context = {
        'data': randomized_quote,
        'image_url' : image_url
    }
    return JsonResponse(
        {'context': context}, status=200
    )
