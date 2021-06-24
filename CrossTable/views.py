from django.shortcuts import render, redirect
from django.urls import reverse
from .calculate import calculate_cross_table

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
        
        temp_column="\tALL ANSWERS FOR MAIN QUESTION\tPERSON DOESN'T HAVE CAT\tPERSON LIVES IN NEW YORK\tQuestion 3\r\nYES\t20,0%\t22,2%\t25,0%\t25,0%\r\nNO\t25,0%\t33,3%\t12,5%\t25,0%\r\nI DON'T KNOW\t15,0%\t11,1%\t25,0%\t12,5%\r\nMAYBE\t15,0%\t11,1%\t12,5%\t12,5%\r\nANSWER 5\t10,0%\t11,1%\t12,5%\t12,5%\r\nANSWER 6\t15,0%\t11,1%\t12,5%\t12,5%\r\n"
        temp_column = temp_column.split("\r\n")
        temp_column0=[]
        for item in temp_column:
            x = item.split("\t")
            temp_column0.append(x)
        temp_column=temp_column0
        print(temp_column)
        context={'temp_column':temp_column}
        return render(request,'CrossTable/setup0.html',context)

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

    columns=[]
    
   
    columns.append((request.POST.get('quesion_0_column')).split("\r\n"))
    print(repr(request.POST.get('quesion_0_column')))
    


    for i in range(1,questions_number_int+1):
        column=request.POST.get(f'quesion_{i}_column')
        columns.append(column.split("\r\n"))

    divided_all=calculate_cross_table(answers_for_columns,columns)
    context={'divided_all':divided_all}
    
    return render(request,'CrossTable/result.html',context)
    