from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Mark, Attendance
from django.contrib.auth.decorators import login_required

def home(request):
    students = Student.objects.all()[:6]
    return render(request, 'core/home.html', {'students': students})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    marks = Mark.objects.filter(student=student)
    attendance = Attendance.objects.filter(student=student).order_by('-date')[:10]
    return render(request, 'core/student_detail.html', {'student': student, 'marks': marks, 'attendance': attendance})

@login_required
def parent_dashboard(request):
    # assume Parent is linked to user
    try:
        parent = request.user.parent
    except Exception:
        return redirect('parent_login')
    student = parent.student
    marks = Mark.objects.filter(student=student)
    attendance = Attendance.objects.filter(student=student).order_by('-date')[:20]
    return render(request, 'core/parent_dashboard.html', {'student': student, 'marks': marks, 'attendance': attendance})
