# coding:utf-8

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Student, Grades

import os
from django.conf import settings


def index(request):
    stu = Student.objects.get(pk=1)
    return render(request, 'myApp/index.html', {'stu': stu, 'num': 10,
    'code':'<h1>This is an html code.</h1>'})


#
# def index(request):
#     return HttpResponse('sam is a good man')


def grades(request):
    # 去模板里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板

    return render(request, 'myApp/grades.html', {'grades': gradesList})


def grade(request, gradeNum):
    # 指定班级里的所有学生
    grade = Grades.objects.get(pk=gradeNum)

    # students_set属性不存在，什么原因？？？？，拼写错误！！！
    '''
    Student的外键是Grades，此处通过外键发生关联过滤
    '''
    studentsOfGrade = grade.student_set.all()

    return render(request, 'myApp/students.html', {'students': studentsOfGrade})


def students(requst):
    studentList = Student.objects.all()
    return render(requst, 'myApp/students.html', {'students': studentList})


def students1(requst):
    studentList = Student.objects.all()
    return render(requst, 'myApp/students1.html',
                  {'students': studentList, 'num': 10, 'str': 'sam is a nice man',
                   'list': ['I', 'love', 'u'],
                   'test': ''})


def student(request, studentId):
    student = Student.objects.get(pk=studentId)
    return render(request, 'myApp/students.html', {'student': student})


def upfile(request):
    return render(request, 'myApp/upfile.html')


def savefile(request):
    if request.method == 'POST':
        f = request.FILES['file']
        filePth = os.path.join(settings.MEDIA_ROOT, f.name)
        with open(filePth, 'wb') as wf:
            for chunk in f.chunks():
                wf.write(chunk)

    else:
        HttpResponse('上传文件失败')


from django.core.paginator import Paginator


def studentPage(request, pageId):
    allList = Student.objects.all()

    paginator = Paginator(allList, 3)

    page = paginator.page(pageId)

    return render(request, 'myApp/studentpage.html',
                  {'students': page})


def ajaxstudens(request):
    return render(request, 'myApp/ajaxstudents.html')


def edit(request):
    return render(request, 'myApp/edit.html')

def main(request):
    return render(request, 'myApp/main.html')

def detail(request):
    return render(request, 'myApp/detail.html')

def postfile(request):
    return render(request, 'myApp/postfile.html')

def showinfo(request):
    name = request.POST.get('username')
    pwd = request.POST.get('password')
    return render(request, 'myApp/showinfo.html', {'name':name, 'password':pwd})