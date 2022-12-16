from django.http import HttpResponse
from django.shortcuts import render

from utils.inserts.factory import make_insert

# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'process': [make_insert() for _ in range(10)],
    })


def insert(request, id):
    return render(request, 'recipes/pages/insert-view.html', context={
        'process': make_insert(),
        'is_detail_page': True
    })
