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
    non_prof_graphs = NonProfConnectedDemandGraph.objects.all()
    prof_graphs = profession.profconnecteddemandgraph_set.all()
    comparison_graphs = profession.comparisondemandgraph_set.all()
    prof_name = profession.name
    context = {
        'non_prof_graphs': non_prof_graphs,
        'prof_graphs': prof_graphs,
        'comparison_graphs': comparison_graphs,
        'prof_name': prof_name
    }
    return render(request, 'profession/demand.html', context=context)


def geography(request):
    return render(request, 'profession/geography.html')


def skills(request):
    return render(request, 'profession/skills.html')


def last_vacancies(request):
    return render(request, 'profession/last-vacancies.html')
