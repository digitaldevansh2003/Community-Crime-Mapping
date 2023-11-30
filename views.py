from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def signin(request):
    return render(request,'Sign-up.html')
def map(request):
    return render(request,'map.html')
