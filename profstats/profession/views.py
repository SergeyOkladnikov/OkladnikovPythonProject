from django.shortcuts import render, HttpResponse
from .models import *


def index(request):
    return render(request, 'profession/index.html')


def demand(request):
    return render(request, 'profession/demand.html')


def geography(request):
    return render(request, 'profession/geography.html')


def skills(request):
    return render(request, 'profession/skills.html')


def last_vacancies(request):
    return render(request, 'profession/last-vacancies.html')
