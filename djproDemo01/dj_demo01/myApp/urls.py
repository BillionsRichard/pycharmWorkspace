from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^grades/$', views.grades),
    url(r'^students/$', views.students),
    url(r'^students1/$', views.students1),

    url(r'^grades/(\d+)$', views.grade),

    url(r'^students/(\d+)$', views.student),
    url(r'^upfile/$', views.upfile),
    url(r'^savefile/$', views.savefile),
    url(r'studentpage/(\d+)$', views.studentPage),
    url(r'ajaxstudents/$', views.ajaxstudens),
    url(r'edit/$', views.edit),

    url(r'^main/$', views.main),
    url(r'^detail/$', views.detail),

    url(r'^postfile/$', views.postfile),
    url(r'^showinfo/$', views.showinfo),
    ]