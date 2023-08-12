from django.shortcuts import render,redirect
from  .models import Task
from  .form import TaskForm,UpdateTaskForm

def index(request):
    todo=Task.objects.all()
    count_todo=todo.count()
    
    complete_todo=Task.objects.filter( complete=True)
    
    count_completed_todo=complete_todo.count()
    
    count_uncompleted_todo=count_todo-count_completed_todo
    
    
    
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=TaskForm()    
        
    
    context={
        'todo':todo,
        'form':form,
        'count_todo':count_todo,
        'count_completed_todo': count_completed_todo,
        'count_uncompleted_todo':count_uncompleted_todo,
    }
    
    return render(request,'index.html',context)


def update(request, pk):
    todo=Task.objects.get(id=pk)
    if request.method=='POST':
        form=UpdateTaskForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=UpdateTaskForm(instance=todo)
        
        
    context={
        
        'form':form
    }
    return render(request,'update.html',context)






def delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'delete.html')


