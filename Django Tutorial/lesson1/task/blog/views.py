from django.shortcuts import render

from .models import Post


def post_list(request):
    get all posts ordered by published_date
    return render(request, 'pass blog/post_list.html template file here', {pass posts object to the template})
