from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    context = {}
    return render(request, "RealEstate/home.html", context)

def contact(request):
    context={}
    return render(request, "Realestate/contact.html", context)