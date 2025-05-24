from django.shortcuts import render

def index1(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')