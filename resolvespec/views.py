from django.shortcuts import render
from resolvespec.models import Node
from django.views.generic.list import ListView
# Create your views here.


class IndexView(ListView):
    template_name = 'resolvespec/index.html'
    context_object_name = 'nodes'

	# def get_queryset(self):
