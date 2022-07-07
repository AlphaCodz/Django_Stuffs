from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task


# Create your views here.
class TaskList(ListView):
    
    model = Task
    context_object_name= 'tasks'
    

class TaskDetail(DetailView):
    model = Task
    context_object_name= 'taskdetail'
    template_name='Check/task_detail.html'
    

# def pending(request):
#     return render(request, 'Pending.html')