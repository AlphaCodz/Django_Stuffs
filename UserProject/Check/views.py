from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Task


# Create your views here.
class TaskList(ListView):
    
    model = Task
    context_object_name= 'tasks'
    

class TaskDetail(DetailView):
    model = Task
    context_object_name= 'taskdetail'
    template_name='Check/task_detail.html'
    

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url= reverse_lazy('task')
    
# def pending(request):
#     return render(request, 'Pending.html')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'