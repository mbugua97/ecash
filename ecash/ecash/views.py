from django.shortcuts import render,HttpResponse

def callback(request):
    return HttpResponse("<h1> this is a test</h1>")