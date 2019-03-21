from django.shortcuts import render
from django.http  import request,HttpResponse
# Create your views here.
def test_Page(request):
    return HttpResponse('hello world!')