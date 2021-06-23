from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'CrossTable/index.html')

def setup1(request,quesion_0_possible_answers_number,questions_number):
    quesion_0_possible_answers_number_int=quesion_0_possible_answers_number
    questions_number_int=questions_number
    quesion_0_possible_answers_number=[*range(1, quesion_0_possible_answers_number+1, 1)]
    questions_number=[*range(1, questions_number+1, 1)]

    context={'quesion_0_possible_answers_number':quesion_0_possible_answers_number,'questions_number':questions_number,
    'quesion_0_possible_answers_number_int':quesion_0_possible_answers_number_int,
    'questions_number_int':questions_number_int}
    return render(request,'CrossTable/setup1.html',context)

def setup0(request):
    
    if request.method=='POST':
        
        quesion_0_possible_answers_number = request.POST.get('quesion_0_possible_answers_number')
        questions_number = request.POST.get('questions_number')
        print("działa")
        print(quesion_0_possible_answers_number)
        kwargs = {'quesion_0_possible_answers_number': quesion_0_possible_answers_number,'questions_number':questions_number}
        return redirect( 'CrossTable:setup1',**kwargs)
    else:
        print("NIE działa")
        return render(request,'CrossTable/setup0.html')

def result(request,quesion_0_possible_answers_number_int,questions_number_int):
    #Root question + other questions
    amount_of_columns = questions_number_int+1
    answers_for_columns=[]

    quesion_0_possible_answers=[]
    for i in range(1,quesion_0_possible_answers_number_int+1):
        quesion_0_possible_answers.append(request.POST.get(f'quesion_0_answer_{i}'))
    answers_for_columns.append(quesion_0_possible_answers)
    print(answers_for_columns)

    
    for i in range(1,questions_number_int+1):
        temp_list=[]
        temp_list.append(request.POST.get(f'quesion_answer_{i}'))
        answers_for_columns.append(temp_list)
    print(answers_for_columns)
    x=request.POST.get('quesion_0_column').replace("\r\n","..")
    print(x)
    for x in range(60):
        if '\n' in str(x):
            print('jest')



    
    
    return render(request,'CrossTable/result.html')
    