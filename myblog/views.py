from django.shortcuts import redirect
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

def home(request):
    return redirect('blog:index')
# views.py

