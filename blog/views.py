from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')
def post(request):
    posts = [
        {
            'title':'Post',
            'text':'A lot of text A lot of text A lot of text A lot of text A lot of text A lot of text A lot of text',
            'created':'2020-07-19 10:30',
        },{
            'title':'Post',
            'text':'A lot of text A lot of text A lot of text A lot of text A lot of text A lot of text A lot of text',
            'created':'2020-07-19 10:57',
        },{
            'title':'Post',
            'text':'A lot of text A lot of text A lot of text A lot of text A lot of text A lot of text A lot of text',
            'created':'2020-07-19 11:40',
        }
    ]
    return render(request, 'post.html',{'data': posts})
def comment(request):
    return render(request, 'comment.html')
def about(request):
    return render(request, 'about.html')


