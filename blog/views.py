from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

def post_list(request):
    return HttpResponse('hello Django')

def view_date(request):
    return HttpResponse(str(timezone.now()))
# Create your views here.
