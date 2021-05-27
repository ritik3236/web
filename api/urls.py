from django.urls import path
from api.views import *

app_name = 'api'
urlpatterns = [
    path('quote', quote_record, name = 'quote'),
    path('upload/', TestView.as_view(), name='upload'),
    path('upload/<int:count>', TestView.as_view(), name='upload'),

]
