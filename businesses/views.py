from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Business
from .forms import BusinessForm
# Create your views here.
# def home(request):
# 	contex = {
# 		'title': 'Random Business',
# 	}
# 	return render(request, 'home.html', contex)

def business_list(request):
	context = {
		"objects": Business.objects.all(),
	}
	return render(request, 'business_list.html', context)

def business_detail(request, business_id):
	context = {
		"business": Business.objects.get(id=business_id),
	}
	return render(request, 'business_detail.html', context)

def business_create(request):
	form = BusinessForm()
	if request.method == "POST":
		form = BusinessForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('business_list')
	context = {
		"form": form,
	}
	return render(request, 'business_create.html', context)

def business_update(request, business_id):
	business_obj = Business.objects.get(id=business_id)
	form = BusinessForm(instance=business_obj)
	if request.method == "POST":
		form = BusinessForm(request.POST, instance=business_obj)
		if form.is_valid():
			form.save()
			return redirect('business_detail', business_id=business_obj.id)
	context = {
		"form": form,
		"obj": business_obj,
	}
	return render(request, 'business_update.html', context)

def business_delete(request, business_id):
	Business.objects.get(id=business_id).delete()
	return redirect('business_list')
