from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^grades/$', views.grades),
    url(r'^students/$', views.students),

    url(r'^grades/(\d+)$', views.grade),

    url(r'^students/(\d+)$', views.student),
    ]