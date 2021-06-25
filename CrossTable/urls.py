from django.contrib import admin
from django.urls import path
from . import views
import CrossTable

app_name='CrossTable'

urlpatterns = [
    path('', views.index, name='index'),
    path('setup0/',
    views.setup0,name='setup0'
    ),
    path('setup1/<int:quesion_0_possible_answers_number_list>/<int:questions_number_list>/',
    views.setup1,name='setup1'
    ),
    path('result/<int:quesion_0_possible_answers_number_int>/<int:questions_number_int>/',
    views.result,name='result')

]
