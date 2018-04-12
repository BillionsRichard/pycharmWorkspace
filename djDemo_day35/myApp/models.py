from django.db import models


# Create your models here.

class Grade(models.Model):
    class Meta:
        db_table = 'grade'

    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField()

    def __str__(self):
        return '%s' % (self.gname)


class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(isDelete=False)

    def createStudent(self, name, age, gender, content, grade, lstTime, createTime, isDelete=False):
        stu = self.model()
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontent = content
        stu.sgrade = grade
        stu.lastTime = lstTime
        stu.createTime = createTime
        stu.isDelete = isDelete

        return stu


class Student(models.Model):
    class Meta:
        db_table = 'student'
        ordering = ['id']

    stuMgr = models.Manager()
    stuMgr1 = StudentManager()

    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField(db_column='age')
    scontent = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    # 关联外键
    sgrade = models.ForeignKey('Grade')
    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now_add=True)

    # 定义一个类方法，创建对象。
    @classmethod
    def createStudent(cls, name, age, gender, content, grade, lstTime, createTime, isDelete=False):
        stu = cls(sname=name, sage=age, sgender=gender,
                  scontent=content, sgrade=grade, lastTime=lstTime, createTime=createTime,
                  isDelete=isDelete)

        return stu

    def __str__(self):
        return self.sname

    def getName(self):
        return self.sname


from tinymce.models import HTMLField


class Text(models.Model):
    str = HTMLField()
