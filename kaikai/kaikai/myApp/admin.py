#coding:utf-8
from django.contrib import admin

# Register your models here.
from .models import Grades,Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        return '男' if self.sgender else '女'

    def content(self):
        return self.scontent

    #设置页面列名称
    gender.short_description = '性别'
    content.short_description = '简介'
    # Student.sgrade.short_description = '班级'



    list_display = ['pk', 'sname', gender, 'sage', content,
                    'sgrade', 'isDelete']
    list_per_page = 2

    #执行动作的位置
    actions_on_top = False
    actions_on_bottom = True


class StudentInfo(admin.TabularInline):
    model = Student
    extra = 2


@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentInfo]
    # 列表页属性
    list_display = ['pk', 'ggirlnum', 'gboynum', 'isDelete', 'gname', 'gdate']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5
    # # 修改页属性
    # fields = ['gname', 'ggirlnum', 'gboynum', 'gdate', 'isDelete']
    fieldsets = [
        ('First', {'fields':['gname', 'gdate']}),
        ('second', {'fields': ['ggirlnum', 'gboynum', 'isDelete']})
    ]




# admin.site.register(Grades, GradesAdmin)
# admin.site.register(Student, StudentAdmin)
