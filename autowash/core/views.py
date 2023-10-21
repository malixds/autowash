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


def expressWash(request):

    return render(request, 'core/expresswash.html')


def contacts(request):

    return render(request, 'core/contacts.html')


def shop(request):

    return render(request, 'core/shop.html')


def euro(request):

    return render(request, 'core/euro.html')\



def nano(request):

    return render(request, 'core/nano.html')


def engine(request):

    return render(request, 'core/engine.html')


def interior(request):

    return render(request, 'core/interior.html')

def cons(request):

    return render(request, 'core/cons.html')

def complexClear(request):

    return render(request, 'core/complexclear.html')

def diskClear(request):

    return render(request, 'core/diskclear.html')

def photo_wash(request):
    return render(request, 'core/photowash.html')

def photo_shop(request):
    return render(request, 'core/photoshop.html')
