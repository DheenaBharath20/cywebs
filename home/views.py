from django.shortcuts import render




def home(request):
    return render(request, "home.html")

def education(request):
    return render(request, "edu.html")

def environment(request):
    return render(request, "env.html")

def socialwelfare(request):
    return render(request,"socwel.html")




