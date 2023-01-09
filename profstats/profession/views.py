from django.shortcuts import render, HttpResponse
from .models import *
from profession.utils import *

if Profession.objects.filter(is_chosen=True):
    profession = Profession.objects.filter(is_chosen=True)[0]
else:
    profession = None


def index(request):
    page = Page.objects.get(name='home')
    context = {
        'page': page,
        'profession': profession
    }
    return render(request, 'profession/index.html', context=context)


def demand(request):
    page = Page.objects.get(name='demand')
    settings = DemandPageSettings.objects.filter(is_chosen=True).last()
    non_prof_graphs = NonProfConnectedGraph.objects.filter(page=page)
    prof_graphs = profession.profconnectedgraph_set.filter(page=page) if profession else None
    comparison_graphs = profession.comparisongraph_set.filter(page=page) if profession else None
    non_prof_table_data = NonProfConnectedTableData.objects.filter(page=page)
    prof_table_data = profession.profconnectedtabledata_set.filter(page=page) if profession else None

    non_prof_tables = open_table_data(non_prof_table_data)
    prof_tables = open_table_data(prof_table_data) if profession else None
    prof_name = profession.name if profession else None
    context = {
        'page': page,
        'settings': settings,
        'non_prof_graphs': non_prof_graphs,
        'prof_graphs': prof_graphs,
        'comparison_graphs': comparison_graphs,
        'prof_name': prof_name,
        'non_prof_tables': non_prof_tables,
        'prof_tables': prof_tables
    }
    return render(request, 'profession/demand.html', context=context)


def geography(request):
    page = Page.objects.get(name='geography')
    settings = GeographyPageSettings.objects.filter(is_chosen=True).last()
    prof_name = profession.name if profession else None
    graphs = NonProfConnectedGraph.objects.filter(page=page)
    table_data = NonProfConnectedTableData.objects.filter(page=page)
    tables = open_table_data(table_data)
    context = {
        'page': page,
        'prof_name': prof_name,
        'graphs': graphs,
        'tables': tables,
        'settings': settings
    }
    return render(request, 'profession/geography.html', context=context)


def skills(request):
    page = Page.objects.get(name='skills')
    settings = SkillsPageSettings.objects.filter(is_chosen=True).last()
    non_prof_graphs = NonProfConnectedGraph.objects.filter(page=page)
    non_prof_table_data = NonProfConnectedTableData.objects.filter(page=page)
    prof_graphs = profession.profconnectedgraph_set.filter(page=page) if profession else None
    table_series_data = profession.tableseriesdata_set.filter(page=page) if profession else None

    prof_name = profession.name if profession else None
    non_prof_tables = open_table_data(non_prof_table_data)
    years_skills_tables = open_table_series_data(table_series_data) if profession else None

    context = {
        'page': page,
        'non_prof_graphs': non_prof_graphs,
        'prof_graphs': prof_graphs,
        'prof_name': prof_name,
        'non_prof_tables': non_prof_tables,
        'years_skills_tables': years_skills_tables,
        'settings': settings
    }
    return render(request, 'profession/skills.html', context=context)


def last_vacancies(request):
    page = Page.objects.get(name='last-vacancies')
    import datetime
    import requests
    today = datetime.datetime.today()
    datetime_to = datetime.datetime(today.year, today.month, 1) - datetime.timedelta(days=1)
    date_from = datetime.datetime(datetime_to.year, datetime_to.month, 1).strftime('%Y-%m-%d')
    date_to = datetime_to.strftime('%Y-%m-%d')

    request = requests.get(f'https://api.hh.ru/vacancies?text=Инженер-программист&search_field=name&date_from={date_from}&date_to={date_to}')
    vacancies = sorted(request.json()['items'], key=lambda x: x['published_at'])[-10:]
    vac_output = []
    for vacancy in vacancies:
        full_vacancy = requests.get(f'https://api.hh.ru/vacancies/{vacancy["id"]}').json()
        vac_output.append(full_vacancy)
    context = {
        'page': page,
        'vacancies': vac_output
    }
    return render(request, 'profession/last-vacancies.html', context=context)
