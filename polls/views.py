from django.http import HttpResponse,HttpResponseRedirect
from django.http.response import Http404
from django.urls import reverse
from django.views.generic.list import ListView
from polls.models import Question,Choice
from django.shortcuts import render,get_object_or_404
from django.views import generic


# def index(request):
#     questions= Question.objects.all()
#     return HttpResponse(render(request, 'polls/anchor.html' , {'questions':questions}))

# def detail(request, question_id):
#     question= get_object_or_404(Question, pk= question_id)
#     return HttpResponse(render(request, 'polls/index.html', {'question':question}))

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

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
    
def owner(request):
    return HttpResponse("Hello, world. 819ba59c is the polls index.")   


class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name= 'questions'

    def get_queryset(self):
        return Question.objects.all()

class DetailView(generic.DetailView):
    model= Question
    template_name='polls/detail.html'

class ResultView(generic.DetailView):
    model= Question
    template_name= 'polls/results.html'
