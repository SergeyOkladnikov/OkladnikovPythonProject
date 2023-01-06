import json
from stats import *

csv_years_path = 'input_data/vacancies_with_skills.csv'
df_years = pd.read_csv(csv_years_path, header=0, dtype={'name': str, 'key_skills': str, 'salary_from': float, 'salary_to': float, 'salary_currency': str, 'published_at': str})

csv_areas_path = 'input_data/vacancies_by_years.csv'
df_areas = pd.read_csv(csv_areas_path, header=0, dtype={'name': str, 'key_skills': str, 'salary_from': float, 'salary_to': float, 'salary_currency': str, 'published_at': str})

years_stats = get_years_stats(df_years, 'Инженер-программист')
areas_stats = get_areas_stats(df_areas, 0.01)
skills_stats = get_skills_stats(df_years, 10)


year_salary_dynamics = years_stats['years_salary_dynamics']
num_of_vacancies_per_year = years_stats['years_vac_num_dynamics']
year_salary_dynamics_for_prof = years_stats['years_salary_dynamics_for_prof']
num_of_vacancies_per_year_for_prof = years_stats['years_vac_num_dynamics_for_prof']

salary_levels_of_areas = areas_stats['salaries_of_areas']
vacancy_fractions_of_areas = areas_stats['vacancy_fractions_of_areas']

top_skills_total = skills_stats['top_skills_total']
top_skills_of_years = skills_stats['top_skills_of_years']


make_hist(year_salary_dynamics, 'Динамика уровня зарплат по годам', 'years_salary')
make_hist(num_of_vacancies_per_year, 'Динамика количества вакансий по годам', 'years_vac_num')
make_hist(year_salary_dynamics_for_prof, 'Динамика уровня зарплат по годам для выбранной профессии', 'years_salary_for_prof')
make_hist(num_of_vacancies_per_year_for_prof, 'Динамика количества вакансий по годам для выбранной профессии', 'years_vac_num_for_prof')
make_comparison_hist(year_salary_dynamics,
                     year_salary_dynamics_for_prof,
                     'Инженер-программист',
                     'Динамика уровня зарплат по годам',
                     'Средняя з/п',
                     'years_salary')

make_comparison_hist(common_stat_dict=num_of_vacancies_per_year,
                     prof_stat_dict=num_of_vacancies_per_year_for_prof,
                     profession='Инженер-программист',
                     title='Динамика количества вакансий по годам',
                     legend='Количество вакансий',
                     name='years_vac_num')
make_inverted_hist(salary_levels_of_areas, 'Уровень зарплат по городам', 'areas_salary')
make_pie(vacancy_fractions_of_areas, 'Доля вакансий по городам', 'areas_vac_fractions')

make_inverted_hist(top_skills_total, 'Топ-10 навыков по кол-ву упоминаний за всё время', 'top_skills_total')

for key, value in top_skills_of_years.items():
    make_inverted_hist(value, f'Топ-10 навыков по кол-ву упоминаний за {key} год', f'top_skills_{key}')

with open('json_files/years_stats.json', 'w') as file:
    json.dump(years_stats, file, ensure_ascii=False, indent=4)

for key in areas_stats['vacancy_fractions_of_areas'].keys():
    areas_stats['vacancy_fractions_of_areas'][key] = "{:.2%}".format(
        float(areas_stats['vacancy_fractions_of_areas'][key]))

with open('json_files/areas_stats.json', 'w') as file:
    json.dump(areas_stats, file, ensure_ascii=False, indent=4)

with open('json_files/skills_stats.json', 'w') as file:
    json.dump(skills_stats, file, ensure_ascii=False, indent=4)