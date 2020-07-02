from django.shortcuts import render, HttpResponse
from django.shortcuts import render	

def index(request):
    return render(request, "new_app/index.html")
    