from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo
from django.urls import reverse
import datetime

def index(request):
    latest_todo_list = Todo.objects.order_by('-pub_date')#[:5]
    context = {'latest_todo_list': latest_todo_list}
    return render(request, 'todo/index.html', context)

def add_todo(request):
    newtodo_text=request.POST['todo_item']
    if newtodo_text:
        t = Todo(todo_text=newtodo_text, pub_date=datetime.date.today())
        t.save()
    return HttpResponseRedirect(reverse('todo:index'))

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        todo.delete()                     # delete the cat.

    return HttpResponseRedirect(reverse('todo:index'))

def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        todo.todo_text = request.POST['todo_text']
        todo.save()                   

    return HttpResponseRedirect(reverse('todo:index'))

def delete_all_todo(request):
    if request.method == 'POST':        
        Todo.objects.all().delete()

    return HttpResponseRedirect(reverse('todo:index'))

def toggle_status_todo(request, todo_id):
    print("dfgdfg")
    # todo = get_object_or_404(Todo, pk=todo_id)  # Get your current cat
    # if request.method == 'POST':        
    #     todo.completion_status = not todo.completion_status

    return 
