from django.http import HttpResponse
from polls.models import Question


def index(request):
    questions= Question.getAllQuestions()
    res=''
    for i in questions:
        res += str(i)
        res +='\n'
    return HttpResponse(res)

def detail(request, question_id):
    question= Question.getQuestionById(question_id)
    return HttpResponse(f'You are looking at question: {question}')

def vote(request, question_id):
    return HttpResponse(f'You are voting at question: {question_id}')

def results(request, question_id):
    return HttpResponse(f'Result {question_id}')    