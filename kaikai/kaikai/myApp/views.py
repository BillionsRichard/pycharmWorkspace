# coding:utf-8

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Student, Grades


def index(request):
    return HttpResponse('sam is a good man')


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


def student(request, studentId):
    student = Student.objects.get(pk=studentId)
    return render(request, 'myApp/students.html', {'student': student})
