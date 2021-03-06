from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.


def treetest(request):
    myTree = {'children': [], 'title': 'Root',
              'isFolder': True, 'hideCheckbox': True}
    myTree['children'].append(
        {'title': 'Child 1', 'isFolder': 'false', 'children': []})
    myTree['children'].append(
        {'title': 'Child 2', 'isFolder': 'false', 'children': []})
    myTree['children'].append(
        {'title': 'Child 3', 'isFolder': 'false', 'children': []})

    # Convert result list to a JSON string
    res = json.dumps(myTree, encoding="Latin-1")

    # Support for the JSONP protocol.
    response_dict = {}
    if request.GET.has_key('callback'):
        response_dict = request.GET['callback'] + "(" + res + ")"

    return HttpResponse(response_dict, mimetype='application/json')

    response_dict = {}
    response_dict.update({'children': tree})
    return HttpResponse(response_dict, mimetype='application/javascript')
