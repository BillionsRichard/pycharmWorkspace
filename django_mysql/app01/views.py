from django.shortcuts import render, HttpResponse
from app01.models import Book

# Create your views here.
"""
表记录的添加
方式一：
    b = Book()
    b.save()
    
方式二、
    Book.objects.create(**kwargs)
    

"""


def index(request):
    return render(request, 'index.html')


def addBook(request):
    b = Book(name='python基础', price=99, author='alex', pub_date='2017-12-12')
    b.save()

    return HttpResponse('添加成功')


def update(request):
    # Book.objects.filter(author='oldboy').update(price=99.9)
    b = Book.objects.filter(author='oldboy')[0]
    b.price = 120
    b.save()
    print(b)
    print(type(b))
    return HttpResponse('修改成功')


def delete(request):
    # Book.objects.filter(author='oldboy').update(price=99.9)
    Book.objects.filter(author='sam').delete()
    return HttpResponse('删除成功')
