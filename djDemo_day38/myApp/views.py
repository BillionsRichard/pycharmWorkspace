from django.shortcuts import render
from myApp.models import Grade,Student

# Create your views here.
def students(request):
    students = Student.stuMgr.all()
    return render(request, '')