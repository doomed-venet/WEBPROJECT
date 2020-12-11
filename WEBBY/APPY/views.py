from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.http import require_POST


# Create your views here.
def hi(request):
    return render(request, 'APPY/hi.html')
