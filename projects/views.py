from django.shortcuts import render

# Create your views here.

def homeview(request):
    context = {}
    return render(request,'index.html',context)
