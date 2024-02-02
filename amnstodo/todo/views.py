from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import TodoForm
from .models import Todo

# Add View 

def add(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        
    else:
        form = TodoForm()
        return render(request,'add.html',{"title":'Add','form':form})

    
# List view 
    
def listd(request):
    todo_obj = Todo.objects.all()
    print(todo_obj)
    return render(request,'list.html',{"title":"TODO List",'obj':todo_obj})

# delete view 

def delete(request,todo_id):
    print("Deleting a item")
    try:
        todos = get_object_or_404(Todo,pk=todo_id)
    except Exception as e:
        return HttpResponse('<b> No More tasks to be deleted </b>')
    todos.delete()
    return redirect('list')
    


