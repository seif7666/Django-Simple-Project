from django.http import HttpResponse,HttpResponseRedirect
from django.http.response import Http404
from django.urls import reverse
from polls.models import Question,Choice
from django.shortcuts import render,get_object_or_404



def index(request):
    questions= Question.objects.all()
    print(questions[0].id)
    return HttpResponse(render(request, 'polls/anchor.html' , {'questions':questions}))

def detail(request, question_id):
    question= Question.getQuestionById(question_id)
    print(question)

    return HttpResponse(render(request, 'polls/index.html', {'question':question}))

def vote(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    try:
        selected_choice= question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/index.html', {
            'question':question,
            'error_message' : "You didn't select a choice!"
        })
    selected_choice.votes +=1
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    
def owner(request):
    return HttpResponse("Hello, world. 819ba59c is the polls index.")   