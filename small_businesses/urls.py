"""small_businesses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from businesses import views

urlpatterns = [
	path('admin/', admin.site.urls),
	# path('home/', include('businesses.urls')),
	path('business_list/', views.business_list, name="business_list"),
	path('business_detail/<int:business_id>/', views.business_detail, name="business_detail"),
	path('business_create/', views.business_create, name="business_create"),
	path('business_update/<int:business_id>/', views.business_update, name="business_update"),
	path('business_delete/<int:business_id>/', views.business_delete, name="business_delete"),
]
