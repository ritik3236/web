from collections import defaultdict
from django.urls import path
from home import views
from home.views import *

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('Q_paper/', QuestionView.as_view(), name='ques'),
    path('Q_paper/<int:c_id>/', QuestionView.as_view(), name='ques'),
    path('Q_paper/<int:c_id>/<int:sem_id>/', QuestionView.as_view(), name='sem'),
    path('Q_paper/<int:c_id>/<int:sem_id>/<str:sub_name>', QuestionView.as_view(), name='subject'),

]
