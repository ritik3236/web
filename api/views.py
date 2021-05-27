from django.views.generic import TemplateView
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render

from api.models import *
from api.forms import *

import random
# Create your views here.


def quote_record(request):
    lst = []
    image_url = []
    q = QuotesApi.objects.all()
    for i in q:
        lst.append(i)
    rq = random.sample(lst, 4)
    for i in rq:
        try:
            image_url.append(i.author_img.url)
        except Exception as e:
            image_url.append('img not found')
    randomized_quote = serializers.serialize('json', rq)
    context = {
        'data': randomized_quote,
        'image_url': image_url
    }
    return JsonResponse(
        {'context': context}, status=200
    )


class TestView(TemplateView):
    template_name = 'upload.html'

    def get(self, request, *args, **kwargs):
        context = {'form': TestForm()}
        return render(request, self.template_name, context)

    def post(self, request, count=0, *args, **kwargs):
        file_upload = FileUpload()
        print(count)
        upload_result = ''
        form = TestForm(request.POST, request.FILES)
        files = request.FILES.getlist('document')
        if form.is_valid():
            for file in files:
                file_upload.name = form.cleaned_data['name']
                file_upload.email = form.cleaned_data['email']
                file_upload.type = form.cleaned_data['type']
                file_upload.document = file
                file_upload.description = form.cleaned_data['description']
                file_upload.save()
                count = count + 1
            upload_result = 'Upload Successful'
        context = {
            'form': TestForm(),
            'upload_result': upload_result,
            'count': count,
        }
        return render(request, self.template_name, context)
