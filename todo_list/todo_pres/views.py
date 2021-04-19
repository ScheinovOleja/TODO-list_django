from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import TasksForm
from .models import TodoList, Category

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView, UpdateView


class AllTasksView(ListView):
    model = TodoList
    template_name = 'todo_pres/main.html'
    context_object_name = 'tasks'


class CreateTaskView(CreateView):
    model = TodoList
    template_name = 'todo_pres/create.html'
    success_url = '/'
    fields = ['title', 'content', 'deadline', 'category']


class DetailTaskView(DetailView):
    model = TodoList
    template_name = 'todo_pres/task_detail.html'
    success_url = '/'
    context_object_name = 'task'

    def post(self, request, pk):
        TodoList.objects.get(id=pk).delete()
        return redirect('all_task')


class EditTaskView(UpdateView):
    model = TodoList
    template_name = 'todo_pres/editing.html'
    success_url = '/'
    fields = ['title', 'content', 'category']


class CategoryView(ListView):
    model = Category
    template_name = 'todo_pres/category.html'
    context_object_name = 'categories'

    def post(self, request):
        if "Add" in request.POST:
            name = request.POST["name"]
            category = Category(name=name)
            category.save()
            return self.get(request)
        if "Delete" in request.POST:
            check = request.POST.getlist('check')
            for i in check:
                try:
                    categories = Category.objects.filter(id=i)
                    for category in categories:
                        category.delete()
                except BaseException:
                    return HttpResponse('<h1>Сначала удалите карточки с этими категориями</h1>')
            return self.get(request)
