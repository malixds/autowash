from django.shortcuts import render

# Create your views here.

def main(request):

    return render(request, 'core/main.html')

def collapse(request):

    return render(request, 'core/collapse.html')

def fitting(request):

    return render(request, 'core/fitting_list.html')

def locksmith(request):

    return render(request, 'core/locksmith.html')

def allServices(request):

    return render(request, 'core/allservices.html')

def wash(request):

    return render(request, 'core/wash.html')
