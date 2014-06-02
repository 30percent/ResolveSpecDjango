from django.shortcuts import render
from resolvespec.models import Node
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'resolvespec/index.html'
    context_object_name = 'nodes'

   # def get_queryset(self):
        
