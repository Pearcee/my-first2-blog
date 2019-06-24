from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse
from .forms import PostForm
from . models import feed
import json
# Create your views here.
def index(request):
	template='posts/index.html'
	results=feed.objects.all()
	jsondata = serializers.serialize('json',results)
	context={
		'results':results,
		'jsondata':jsondata,
	}
	return render(request,template,context)

def getdata(request):
	results=feed.objects.all()
	jsondata = serializers.serialize('json',results)
	return HttpResponse(jsondata)

def base_layout(request):
	template='posts/base.html'
	return render(request,template)

def about_layout(request):
	template='posts/about.html'
	return render(request,template)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'posts/post_edit.html', {'form': form})