# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'index.html')

def projects(request):
	return render(request, 'index.html')

def experimental(request):
	return render(request, 'index.html')