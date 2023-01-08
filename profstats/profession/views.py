from django.shortcuts import render, HttpResponse
from .models import *
import json
from profession.utils import *

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
    non_prof_graphs = NonProfConnectedGraph.objects.filter(page_id='2')
    prof_graphs = profession.profconnectedgraph_set.filter(page_id='2') if profession else None
    comparison_graphs = profession.comparisongraph_set.filter(page_id='2') if profession else None
    non_prof_table_data = NonProfConnectedTableData.objects.filter(page_id='2')
    prof_table_data = profession.profconnectedtabledata_set.filter(page_id='2') if profession else None

    non_prof_tables = open_table_data(non_prof_table_data)
    prof_tables = open_table_data(prof_table_data) if profession else None
    prof_name = profession.name if profession else None
    context = {
        'non_prof_graphs': non_prof_graphs,
        'prof_graphs': prof_graphs,
        'comparison_graphs': comparison_graphs,
        'prof_name': prof_name,
        'non_prof_tables': non_prof_tables,
        'prof_tables': prof_tables
    }
    return render(request, 'profession/demand.html', context=context)


def geography(request):
    page_id = 3
    prof_name = profession.name if profession else None
    graphs = NonProfConnectedGraph.objects.filter(page_id=page_id)
    table_data = NonProfConnectedTableData.objects.filter(page_id=page_id)
    tables = open_table_data(table_data)
    context = {
        'prof_name': prof_name,
        'graphs': graphs,
        'tables': tables
    }
    return render(request, 'profession/geography.html', context=context)


def skills(request):
    page_id = 4
    non_prof_graphs = NonProfConnectedGraph.objects.filter(page_id=page_id)
    non_prof_table_data = NonProfConnectedTableData.objects.filter(page_id=page_id)
    prof_graphs = profession.profconnectedgraph_set.filter(page_id=page_id) if profession else None
    table_series_data = profession.tableseriesdata_set.filter(page_id=page_id) if profession else None

    prof_name = profession.name if profession else None
    non_prof_tables = open_table_data(non_prof_table_data)
    years_skills_tables = open_table_series_data(table_series_data) if profession else None

    context = {
        'non_prof_graphs': non_prof_graphs,
        'prof_graphs': prof_graphs,
        'prof_name': prof_name,
        'non_prof_tables': non_prof_tables,
        'years_skills_tables': years_skills_tables
    }
    return render(request, 'profession/skills.html', context=context)


def last_vacancies(request):
    return render(request, 'profession/last-vacancies.html')
