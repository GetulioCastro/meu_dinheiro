from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def principal(request):
    template_name = 'base.html'
    return render(request, template_name, {})
