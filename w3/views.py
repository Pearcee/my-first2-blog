from django.shortcuts import render


def index(request):
    return render(request, 'w3/index.html')
