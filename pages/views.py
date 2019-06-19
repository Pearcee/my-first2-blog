from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')

def contact(request):
    return render(request, 'pages/contact.html')

def blank(request):
    return render(request, 'pages/blank.html')