from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home page',
        'content': 'Главная страница магазниа HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': True
    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')
