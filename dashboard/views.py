from django.shortcuts import render

# Create your views here.
def displayHome(request):
    return render(request,'index.html')