from django.shortcuts import render


def home(request):
    return render(request,"autenticat/home.html",{})


# Create your views here.
