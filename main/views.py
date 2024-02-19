from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):


    context = {
        'title': 'MilSim-наши игры ваше удовольствие',
        'content': "",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': "Тут информация о нас"
    }

    return render(request, 'main/about.html', context)