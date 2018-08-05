from django.shortcuts import render,HttpResponse
import time
# Create your views here.

def show_time(request):
    # return HttpResponse('hello')
    t = time.ctime()
    return render(request, "show_time.html", {'t': t})