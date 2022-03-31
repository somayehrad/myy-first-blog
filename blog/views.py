from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request,'blog/post_list.html',{'posts':posts})
    # return HttpResponse('hello Django')

def view_date(request):
    return HttpResponse(str(timezone.now()))
# Create your views here.

def view_cv(request):
    return HttpResponse('somayeh rad cv')


def post_details(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_details.html',{'post':post})

