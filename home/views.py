from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView
from home.models import *


def sort_by_values(dic=None):
    if dic:
        return {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}


def txt_to_list(txt, spacer=' '):
    return(txt.split(spacer))


def func_course_list():
    context = {}
    if Course.objects.all().exists():
        for obj in Course.objects.all().iterator():
            context.update({str(obj.id): obj.c_name})
        return sort_by_values(context).items()
    return ('1', 'No Data')

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *arg, **kwargs):
        sem_list = {'1': '1st', '2': '2nd', '3': '3rd',
                    '4': '4th', '5': '5th', '6': '6th'}
        context = {
            'course_list': func_course_list(),
            'sem_list': sem_list,
            'sub_list': txt_to_list('Plz select Course & semester 👈'),
            'qes_list': ['Plz Select Any Subject 📚 '],
        }
        return render(request, self.template_name, context)


class QuestionView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, sem_id=1, sub_name='Hindi', *args, **kwargs):
        qes_list = ['Plz Select Subject']
        sem_list = {'1': '1st', '2': '2nd', '3': '3rd',
                    '4': '4th', '5': '5th', '6': '6th'}
        if Subject.objects.filter(course_name_id__pk=kwargs['c_id']).exists():
            s = Subject.objects.get(course_name_id__pk=kwargs['c_id'])
            sub_list = list(s.sub_names.split(","))
            ques_result = QuesPaper.objects.filter(
                course_name=kwargs['c_id'], semester=sem_id, sub_name=sub_name.lower())
            for q in ques_result:
                qes_list = list(q.fl_id.split(","))
            if qes_list[0] == 'Plz Select Subject':
                qes_list = [' Unfortunately We Got No Qestion Paper 😔 ']
            else:
                for i in qes_list:
                    q_paper = []
                    try: 
                        q_paper = QuesPaperMedia.objects.get(fl_id = i.lower())
                        print(q_paper.file_name)
                        print(q_paper.file_date)
                    except QuesPaperMedia.DoesNotExist:
                        q_paper = None
        else:
            sub_list = txt_to_list('Sorry We Got No Subjects 😔')
        context = {
            'course_list': func_course_list(),
            'id': kwargs['c_id'],
            'sem_id': sem_id,
            'sem_list': sem_list,
            'sub_list': sub_list,
            'sub_name': sub_name,
            'qes_list': qes_list,
        }
        return render(request, self.template_name, context)
