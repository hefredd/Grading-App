from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Mark
from .forms import MarkForm
from django.contrib import messages
# Create your views here.

def student_list(request):
    students = Student.objects.all()  
    return render(request, 'students.html', {'students': students})

def add_marks(request):
    if request.method == 'POST':
        form = MarkForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = MarkForm()
    return render(request, 'add_marks.html', {'form': form})

def edit_marks(request, mark_id):
    mark = get_object_or_404(Mark, id=mark_id)
    
    if request.method == 'POST':
        form = MarkForm(request.POST, instance=mark)
        if form.is_valid():
            form.save()
            messages.success(request, "Marks updated successfully!")
            return redirect('student_list')
    else:
        form = MarkForm(instance=mark)  
    
    return render(request, 'edit_marks.html', {'form': form, 'mark': mark})

def delete_marks(request, mark_id):
    mark = get_object_or_404(Mark, id=mark_id)
    
    if request.method == 'POST':         
        mark.delete()
        messages.success(request, "Mark deleted successfully!")
        return redirect('student_list')
    
    return render(request, 'delete_marks.html', {'mark': mark})