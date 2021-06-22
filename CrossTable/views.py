from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'CrossTable/index.html')

def setup1(request,quesion_0_possible_answers_number,questions_number):
    quesion_0_possible_answers_number=[*range(1, quesion_0_possible_answers_number+1, 1)]
    questions_number=[*range(1, questions_number+1, 1)]
    context={'quesion_0_possible_answers_number':quesion_0_possible_answers_number,'questions_number':questions_number}
    return render(request,'CrossTable/setup1.html',context)