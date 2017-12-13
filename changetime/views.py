# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import TimeDatas

# Create your views here.
class ModifyView(generic.DetailView):
	model = TimeDatas
	template_name = 'changetime/modify.html'

class ResultsView(generic.DetailView):
    model = TimeDatas
    template_name = 'changetime/results.html'

def change(request):
	changetime = request.POST['modifytime']
	return render(request, 'changetime/results.html', {'changetime': changetime,})
	
