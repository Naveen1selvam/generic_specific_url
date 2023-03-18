from django.shortcuts import render

# Create your views here.
def chill(request):
    return render(request,'chill.html')