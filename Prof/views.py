from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Worker, Counter


def show(request):

		pl = Counter.objects.get(pk=1)
		pl.cnt = pl.cnt +1;
		pl.save()
		
		return render(request,'Prof/list.html',{'wks':Worker.objects.all(),'counter':pl.cnt})

