from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    posts=Posts.objects.all()[:10]
    context={
    	'title': 'Latest Posts',
    	'posts': posts
    }
    return render(request, 'firstapp/index.html', context)

def details(request, id):
	posts=Posts.objects.get(id=id)
	context={
		'posts':posts
	}
	return render(request, 'firstapp/details.html', context)

