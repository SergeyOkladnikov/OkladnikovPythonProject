import json

from django.shortcuts import render, HttpResponse
from .models import *

if Profession.objects.filter(is_chosen=True):
    profession = Profession.objects.filter(is_chosen=True)[0]
else:
    profession = None


def index(request):
    context = {
        'text_1': profession.text_block_1,
        'image_1': profession.image_1,
        'image_1_caption': profession.image_1_caption,
        'text_2': profession.text_block_2,
        'image_2': profession.image_2,
        'image_2_caption': profession.image_2_caption,
        'text_3': profession.text_block_3,
        'image_3': profession.image_3,
        'image_3_caption': profession.image_3_caption,
    }
    return render(request, 'profession/index.html', context=context)


def demand(request):
    with open(profession.years_stats.url[1:], 'r') as file:
        year_stats = json.load(file)
    years_salary_dynamics = dict(sorted(year_stats['years_salary_dynamics'].items(), key=lambda x: x[0]))
    years_vac_num_dynamics = dict(sorted(year_stats['years_vac_num_dynamics'].items(), key=lambda x: x[0]))
    years_salary_dynamics_for_prof = dict(sorted(year_stats['years_salary_dynamics_for_prof'].items(), key=lambda x: x[0]))
    years_vac_num_dynamics_for_prof = dict(sorted(year_stats['years_vac_num_dynamics_for_prof'].items(), key=lambda x: x[0]))

    context = {
        'profession': profession,
        'years_salary_dynamics': years_salary_dynamics,
        'years_vac_num_dynamics': years_vac_num_dynamics,
        'years_salary_dynamics_for_prof': years_salary_dynamics_for_prof,
        'years_vac_num_dynamics_for_prof': years_vac_num_dynamics_for_prof,
    }
    return render(request, 'profession/demand.html', context=context)


def geography(request):
    return render(request, 'profession/geography.html')


def skills(request):
    return render(request, 'profession/skills.html')


def last_vacancies(request):
    return render(request, 'profession/last-vacancies.html')
