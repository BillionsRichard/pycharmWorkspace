from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Max,Min
from myApp.models import Student, Grade


# Create your views here.

def students(request):
    # studentList = Student.stuMgr.all()
    # # maxAge = Student.stuMgr.aggregate(Max('sage'))
    # # print('max age:%s' %maxAge)

    # studentList = Student.stuMgr.filter(Q(pk__lte=12) | Q(sage__gt=27))
    studentList = Student.stuMgr.filter(~Q(pk__lte=12))#取反

    return render(request, 'myApp/students.html',
                  {'students': studentList})

def students2(request):
    # studentList = Student.stuMgr.all()
    # Get只能返回单个符合条件得数据，如果多个会抛出MultipleObjectsReturned异常。
    studentList = Student.stuMgr.get(sgender=True)

def students3(request):
    studentList = Student.stuMgr.all()[:5]
    # Get只能返回单个符合条件得数据，如果多个会抛出MultipleObjectsReturned异常。
    # studentList = Student.stuMgr.get(sgender=True)

    return render(request, 'myApp/students.html',
                  {'students': studentList})

def stuSearch(request, keyWord):
    print(keyWord)
    studentList = Student.stuMgr.filter(sname__contains=keyWord)
    # Get只能返回单个符合条件得数据，如果多个会抛出MultipleObjectsReturned异常。
    # studentList = Student.stuMgr.get(sgender=True)

    return render(request, 'myApp/students.html',
                  {'students': studentList})

def stupage(request, pageNum):
    """返回第pageNum页面
    第一页：0~5
    第二页：5~10
            ...

    :param request:
    :param pageNum:
    :return:
    """
    pageNum = int(pageNum)
    tot = Student.stuMgr.count()
    start = (pageNum-1) * 5
    end = start + 5

    studentList = Student.stuMgr.all()[start:end]
    # Get只能返回单个符合条件得数据，如果多个会抛出MultipleObjectsReturned异常。
    # studentList = Student.stuMgr.get(sgender=True)

    return render(request, 'myApp/students.html',
                  {'students': studentList})


def addStudent(request):
    grade = Grade.objects.get(pk=1)
    # name, age, gender, content, grade, lstTime, createTime, isDelete=False
    stu = Student.createStudent('风清扬', 26, True, '我是风清扬，请多关照',
                                grade,
                                '2018-04-05',
                                '2018-04-05')

    stu.save()

    return HttpResponse('添加%s成功' % stu.sname)

def addStudent1(request):
    grade = Grade.objects.get(pk=2)
    # name, age, gender, content, grade, lstTime, createTime, isDelete=False
    stu = Student.stuMgr1.createStudent('张无忌', 26, True, '我是张无忌，请多关照',
                                grade,
                                '2018-04-05',
                                '2018-04-05')

    stu.save()

    return HttpResponse('添加%s成功' % stu.sname)

from django.db.models import F,Q
def grades(request):
    grades = Grade.objects.filter(ggirlnum__gt=F('gboynum'))
    print(grades)
    return HttpResponse('找到女生人数大于男生人数的班级')