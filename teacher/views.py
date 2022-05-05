from django.shortcuts import render

def teacher_dashboard(request):
    return render(request,'teacher/teacher_dashboard.html')
    