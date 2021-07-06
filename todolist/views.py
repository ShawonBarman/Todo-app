from django.shortcuts import render, redirect
from .models import ToDoList
from .forms import ToDoListForm
from django.views.decorators.http import require_POST

# Create your views here.

def home(request):
    todo_items = ToDoList.objects.order_by("id")
    form = ToDoListForm()
    context = {'todo_items' : todo_items, 'form':form}
    return render(request, 'todolist/index.html', context)

@require_POST
def addToDoItem(request):
    form = ToDoListForm(request.POST)
    # print(request.POST['text'])
    if form.is_valid():
        new_todo = ToDoList(text=request.POST['text'])
        new_todo.save()
    return redirect('home')

def completedToDo(request, todo_id):
    todo = ToDoList.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('home')

def deleteCompleted(request):
    ToDoList.objects.filter(complete__exact=True).delete()
    return redirect('home')

def deleteAll(request):
    ToDoList.objects.all().delete()
    return redirect('home')