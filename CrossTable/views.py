from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'CrossTable/index.html')

def setup1(request,quesion_0_possible_answers_number,questions_number):
    quesion_0_possible_answers_number=[*range(1, quesion_0_possible_answers_number+1, 1)]
    questions_number=[*range(1, questions_number+1, 1)]
    context={'quesion_0_possible_answers_number':quesion_0_possible_answers_number,'questions_number':questions_number}
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

def result(request):
    x=request.POST.get('quesion_answer_1')
    print(x)
    x=request.POST.get('quesion_answer_2')
    print(x)
    #if request.POST.get('quesion_answer_2'):
    #    print('2 jest')
    
    return render(request,'CrossTable/result.html')
    