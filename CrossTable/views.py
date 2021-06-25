from django.shortcuts import render, redirect
from django.urls import reverse
from .calculate import calculate_cross_table,format_output_for_excel


def index(request):
    return render(request, 'CrossTable/index.html')

def setup1(request,quesion_0_possible_answers_number_list,questions_number_list):

    # Converting int values to list to loop through it easly in template
    quesion_0_possible_answers_number_int=quesion_0_possible_answers_number_list
    questions_number_int=questions_number_list
    quesion_0_possible_answers_number_list=[*range(1, quesion_0_possible_answers_number_list+1, 1)]
    questions_number_list=[*range(1, questions_number_list+1, 1)]

    context={'quesion_0_possible_answers_number_list':quesion_0_possible_answers_number_list,'questions_number_list':questions_number_list,
    'quesion_0_possible_answers_number_int':quesion_0_possible_answers_number_int,
    'questions_number_int':questions_number_int}
    return render(request,'CrossTable/setup1.html',context)

def setup0(request):
    
    if request.method=='POST':
        
        # Gets value of two variables in post and passes them to setup1 view
        quesion_0_possible_answers_number_list = request.POST.get('quesion_0_possible_answers_number_list')
        questions_number_list = request.POST.get('questions_number_list')
        
        kwargs = {'quesion_0_possible_answers_number_list': quesion_0_possible_answers_number_list,'questions_number_list':questions_number_list}
        return redirect( 'CrossTable:setup1',**kwargs)
    else:
        
        return render(request,'CrossTable/setup0.html')

def result(request,quesion_0_possible_answers_number_int,questions_number_int):
    
    #Root question + other questions
    answers_for_columns=[]

    # Gets values of input of quesion_0_possible_answers from template and appends them to list

    quesion_0_possible_answers=[]

    for i in range(1,quesion_0_possible_answers_number_int+1):
        quesion_0_possible_answers.append(request.POST.get(f'quesion_0_answer_{i}'))
    answers_for_columns.append(quesion_0_possible_answers)
    
    # Gets values of input of quesion_answers from template and appends them to list
    
    for i in range(1,questions_number_int+1):
        temp_list=[]
        temp_list.append(request.POST.get(f'quesion_answer_{i}'))
        answers_for_columns.append(temp_list)
    

    columns=[]

    # Gets quesion_0_column as string, converts it to list, and appedends to columns list

    columns.append((request.POST.get('quesion_0_column')).split("\r\n"))
    
    
    # Gets quesion_{i}_columns as string, converts it to list, and appedends to columns list

    for i in range(1,questions_number_int+1):
        column=request.POST.get(f'quesion_{i}_column')
        columns.append(column.split("\r\n"))

    divided_all=calculate_cross_table(answers_for_columns,columns)
    output=format_output_for_excel(answers_for_columns,divided_all,questions_number_int,quesion_0_possible_answers_number_int)
    
    context={'output':output}
    
    return render(request,'CrossTable/result.html',context)
    