from django.shortcuts import render

# Create your views here.


def home(req):
	return render(req,"home.html")


def app(req):
	return render(req,"app.html")