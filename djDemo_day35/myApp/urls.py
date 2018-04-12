from django.conf.urls import url
from myApp import views

urlpatterns = [
    url(r'^students/$', views.students),
    url(r'^students2/$', views.students2),
    url(r'^students3/$', views.students3),
    url(r'^stupage/(\d+)/$', views.stupage),
    url(r'^search/(.*)/$', views.stuSearch),
    url(r'^addStudent/$', views.addStudent),
    url(r'^addStudent1/$', views.addStudent1),
    url(r'girlnumgtboynum/$', views.grades),
]