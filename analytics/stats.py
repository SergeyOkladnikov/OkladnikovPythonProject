import pandas as pd
import numpy as np
from itertools import islice

import matplotlib.pyplot as pyplot


currency_to_rub = {
        "AZN": 35.68,
        "BYR": 23.91,
        "EUR": 59.90,
        "GEL": 21.74,
        "KGS": 0.76,
        "KZT": 0.13,
        "RUR": 1,
        "UAH": 1.64,
        "USD": 60.66,
        "UZS": 0.0055,
    }


def extend_dict(shorter, longer):
    for key in longer.keys():
        if key not in shorter.keys():
            shorter[key] = 0
    return shorter


def get_first_dict_elements(dictionary, n):
    result = {}
    if n < 0:
        raise ValueError('index out of range')
    for key in list(islice(dictionary, n)):
        result[key] = dictionary[key]
    return result


def get_mean_salary_in_rur(x):
    return int((float(x['salary_to']) + float(x['salary_from'])) / 2 * currency_to_rub[x['salary_currency']])


def get_years_stats(data, profession):
    data.published_at = pd.to_datetime(data.published_at, utc=True)
    data['year'] = data.published_at.dt.to_period('Y').apply(lambda x: int(str(x)))
    # data_full_salary = data.loc[(data.salary_from.apply(lambda x: str(x)) != 'nan') & (data.salary_to.apply(lambda x: str(x)) != 'nan')]
    data_full_salary = data.dropna(subset = ['salary_to', 'salary_from'])
    data_full_salary['rur_mean_salary'] = data_full_salary.apply(get_mean_salary_in_rur, axis=1)

    years_salary_dynamics = data_full_salary.groupby('year')['rur_mean_salary'].mean().agg(lambda x: int(x)).to_dict()
    years_vac_num_dynamics = data.groupby('year')['name'].count().agg(lambda x: int(x)).to_dict()

    years_salary_dynamics_for_prof = data_full_salary.loc[data_full_salary['name'].apply(lambda x: profession in x)].groupby('year')['rur_mean_salary'].mean().agg(lambda x: int(x)).to_dict()
    years_vac_num_dynamics_for_prof = data_full_salary.loc[data_full_salary['name'].apply(lambda x: profession in x)].groupby('year')['name'].count().agg(
        lambda x: int(x)).to_dict()

    return {'years_salary_dynamics': years_salary_dynamics,
            'years_vac_num_dynamics': years_vac_num_dynamics,
            'years_salary_dynamics_for_prof': years_salary_dynamics_for_prof,
            'years_vac_num_dynamics_for_prof': years_vac_num_dynamics_for_prof}


def get_areas_stats(data, area_frac_threshold):
    total_vacancies = data.shape[0]
    # data_full_salary = data.loc[(data.salary_from.apply(lambda x: str(x)) != 'nan') & (data.salary_to.apply(lambda x: str(x)) != 'nan')]
    data_full_salary = data.dropna(subset = ['salary_to', 'salary_from'])
    data_full_salary['rur_mean_salary'] = data_full_salary.apply(get_mean_salary_in_rur, axis=1)

    vacancy_fractions_of_areas = data.groupby('area_name')['name'].count().agg(lambda x: int(x) / total_vacancies)
    vacancy_fractions_of_areas = pd.Series(vacancy_fractions_of_areas).where(
        lambda x: x >= area_frac_threshold).dropna().sort_values(ascending=False).to_dict()

    salaries_of_areas = data_full_salary.loc[data_full_salary.area_name.apply(lambda x: x in vacancy_fractions_of_areas.keys())].groupby(
        'area_name')['rur_mean_salary'].mean().agg(lambda x: int(x)).sort_values(ascending=False).to_dict()

    return {
        'salaries_of_areas': salaries_of_areas,
        'vacancy_fractions_of_areas': vacancy_fractions_of_areas
    }


def get_skills_stats(data, count_to_show):
    ks = data.dropna(subset=['key_skills'])
    ks.published_at = pd.to_datetime(ks.published_at, utc=True)
    ks['year'] = ks.published_at.dt.to_period('Y').apply(lambda x: int(str(x)))
    ks.key_skills = ks.key_skills.apply(lambda x: x.split('\n'))
    top_skills_total = pd.Series(np.concatenate([x for x in ks.key_skills])).value_counts().head(10).to_dict()
    skills_of_years = ks.groupby('year')['key_skills'].apply(lambda x: pd.Series(np.concatenate([item for item in x])).value_counts().head(10))
    top_skills_of_years = {}
    for index in skills_of_years.index:
        top_skills_of_years[index[0]] = skills_of_years[index[0]].to_dict()
    return {
        'top_skills_total': top_skills_total,
        'top_skills_of_years': top_skills_of_years
    }

def make_hist(stat_dict, title, name):
    fig = pyplot.figure()
    graph = fig.add_subplot(1, 1, 1)
    col_width = 0.8
    x_axis = np.arange(len(stat_dict.keys()))
    graph.bar(x_axis, stat_dict.values(), width=col_width)
    graph.set(title=title, xticks=x_axis)
    graph.set_xticklabels(labels=stat_dict.keys(), rotation='vertical', va='top', ha='center')
    graph.tick_params(axis='both', labelsize=8)
    graph.grid(True, axis='y')
    pyplot.savefig(f'graphs/{name}_hist.png', dpi=300)


def make_comparison_hist(common_stat_dict, prof_stat_dict, profession, title, legend, name):
    fig = pyplot.figure()
    graph = fig.add_subplot(1, 1, 1)
    col_width = 0.4
    x_axis = np.arange(len(common_stat_dict.keys()))
    graph.set_title(title)
    graph.bar(x_axis - col_width / 2, common_stat_dict.values(), width=col_width, label=legend)
    graph.bar(x_axis + col_width / 2, extend_dict(prof_stat_dict, common_stat_dict).values(), width=col_width, label=f'{legend}\n{profession}')
    graph.set_xticks(ticks=x_axis)
    graph.set_xticklabels(labels=common_stat_dict.keys(), rotation='vertical', va='top', ha='center')
    graph.tick_params(axis='both', labelsize=8)
    graph.grid(True, axis='y')
    graph.legend(fontsize=8)
    pyplot.savefig(f'graphs/{name}_comparison_hist.png', dpi=300)


def make_inverted_hist(stat_dict, title, name):
    fig = pyplot.figure()
    graph = fig.add_subplot(1, 1, 1)
    col_width = 0.8
    result_dic = get_first_dict_elements(stat_dict, 13)
    graph.set_title(title)
    graph.invert_yaxis()
    areas = list(result_dic.keys())
    areas = [area.replace(' ', '\n').replace('-', '-\n') for area in areas]
    graph.barh(areas, list(result_dic.values()))
    graph.tick_params(axis='both', labelsize=8)
    graph.set_yticklabels(areas, fontsize=6, va='center', ha='right')
    graph.grid(True, axis='x')
    pyplot.savefig(f'graphs/{name}_inverted_hist.png', dpi=300)


def make_pie(stat_dict, title, name):
    fig = pyplot.figure()
    graph = fig.add_subplot(1, 1, 1)
    result_dic = get_first_dict_elements(stat_dict, 13)
    others = 1 - sum((list(result_dic.values())))
    result_dic.update({'Другие': others})
    labels = list(result_dic.keys())
    graph.pie(list(result_dic.values()), labels=labels, textprops={'fontsize': 6})
    graph.axis('scaled')
    graph.set_title(title)
    pyplot.tight_layout()
    pyplot.savefig(f'graphs/{name}_pie.png', dpi=300)