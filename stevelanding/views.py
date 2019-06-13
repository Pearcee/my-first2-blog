from django.shortcuts import render

# Create your views here.

def sp_index(request):
	template='stevelanding/index.html'
	return render(request,template)