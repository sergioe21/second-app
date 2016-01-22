from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import worker

def show(request):

		
		return render(request,'Prof/list.html',{'wks':worker.objects.all()})

def details(request):


	return HttpResponse('Aloha')