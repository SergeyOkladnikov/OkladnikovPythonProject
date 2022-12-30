from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('Главная')


def demand(request):
    return HttpResponse('Востребованность')


def geography(request):
    return HttpResponse('География')


def skills(request):
    return HttpResponse('Навыки')


def last_vacancies(request):
    return HttpResponse('Последние вакансии')
