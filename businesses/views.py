from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	contex = {
		'title': 'Random Business',
	}
	return render(request, 'home.html', contex)