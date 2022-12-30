from django.shortcuts import render, HttpResponse
from .models import *

nav_elements = NavElement.objects.all()


def index(request):
    context = {'nav_elements': nav_elements}
    return render(request, 'profession/index.html', context)


def demand(request):
    context = {'nav_elements': nav_elements}
    return render(request, 'profession/demand.html', context)


def geography(request):
    context = {'nav_elements': nav_elements}
    return render(request, 'profession/geography.html', context)


def skills(request):
    context = {'nav_elements': nav_elements}
    return render(request, 'profession/skills.html', context)


def last_vacancies(request):
    context = {'nav_elements': nav_elements}
    return render(request, 'profession/last-vacancies.html', context)
