from django.http import HttpResponse
from django.http.response import Http404
from polls.models import Question
from django.shortcuts import render



def index(request):
    questions= Question.getAllQuestions()
    res=''
    for i in questions:
        res += str(i)
        res +='\n'
    return HttpResponse(res)

def detail(request, question_id):
    question= Question.getQuestionById(2)
    question= {'text':question, 'id':1}
    return HttpResponse(render(request, 'polls/anchor.html', question))

def vote(request, question_id):
    return HttpResponse(f'You are voting at question: {question_id}')

def results(request, question_id):
    return HttpResponse(f'Result {question_id}') 

def owner(request):
    return HttpResponse("Hello, world. 819ba59c is the polls index.")   