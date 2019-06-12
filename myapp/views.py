from django.shortcuts import render


def index(request):
    template = 'myapp/index.html'
    return render(request, template)
