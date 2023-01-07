from django.shortcuts import render, HttpResponse
from .models import *

if Profession.objects.filter(is_chosen=True):
    profession = Profession.objects.filter(is_chosen=True)[0]
else:
    profession = None


def index(request):
    context = {
        'profession': profession
    }
    return render(request, 'profession/index.html', context=context)


def demand(request):
    return render(request, 'profession/demand.html')


def geography(request):
    return render(request, 'profession/geography.html')


def skills(request):
    return render(request, 'profession/skills.html')


def last_vacancies(request):
    return render(request, 'profession/last-vacancies.html')
