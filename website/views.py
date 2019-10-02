# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
	render(request, 'index.html')

def projects(request):
	render(request, 'index.html')

def experimental(request):
	render(request, 'index.html')