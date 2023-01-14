import json
from stats import *

csv_skills_path = 'input_data/vacancies_with_skills.csv'
csv_years_path = 'input_data/vacancies_dif_currencies.csv'

prof = 'Инженер-программист'

df_skills = pd.read_csv(csv_skills_path, header=0, dtype={'name': str, 'key_skills': str, 'salary_from': float, 'salary_to': float, 'salary_currency': str, 'published_at': str})
df_years = pd.read_csv(csv_years_path, header=0, dtype={'name': str, 'key_skills': str, 'salary_from': float, 'salary_to': float, 'salary_currency': str, 'published_at': str})

df_skills.published_at = pd.to_datetime(df_skills.published_at, utc=True)
df_skills['year'] = df_skills.published_at.dt.to_period('Y').apply(lambda x: int(str(x)))

df_years.published_at = pd.to_datetime(df_years.published_at, utc=True)
df_years['year'] = df_years.published_at.dt.to_period('Y').apply(lambda x: int(str(x)))

year_salary_dynamics = get_years_salary_dynamics(df_years)
num_of_vacancies_per_year = get_years_vac_num_dynamics(df_years)
year_salary_dynamics_for_prof = get_years_salary_dynamics_for_prof(df_years, profession=prof)
num_of_vacancies_per_year_for_prof = get_years_vac_num_dynamics_for_prof(df_years, profession=prof)
vacancy_fractions_of_areas = get_vacancy_fractions_of_areas(df_years, 0.01)
salary_levels_of_areas = get_salaries_of_areas(df_years, vacancy_fractions_of_areas)
top_skills_total = get_top_skills_total(df_skills)
top_skills_of_years = get_top_skills_of_years(df_skills, profession=prof)

make_hist(year_salary_dynamics, 'Динамика уровня зарплат по годам', 'years_salary')
make_hist(num_of_vacancies_per_year, 'Динамика количества вакансий по годам', 'years_vac_num')
make_hist(year_salary_dynamics_for_prof, f'Динамика уровня зарплат по годам\n для профессии {prof}', 'years_salary_for_prof')
make_hist(num_of_vacancies_per_year_for_prof, f'Динамика количества вакансий по годам\n для профессии {prof}', 'years_vac_num_for_prof')
make_comparison_hist(year_salary_dynamics,
                     year_salary_dynamics_for_prof,
                     prof,
                     'Динамика уровня зарплат по годам',
                     'Средняя з/п',
                     'years_salary')

make_comparison_hist(common_stat_dict=num_of_vacancies_per_year,
                     prof_stat_dict=num_of_vacancies_per_year_for_prof,
                     profession=prof,
                     title='Динамика количества вакансий по годам',
                     legend='Количество вакансий',
                     name='years_vac_num')
make_inverted_hist(salary_levels_of_areas, 'Уровень зарплат по городам', 'areas_salary')
make_pie(vacancy_fractions_of_areas, 'Доля вакансий по городам', 'areas_vac_fractions')

make_inverted_hist(top_skills_total, 'Топ-10 навыков по кол-ву упоминаний за всё время', 'top_skills_total')
for key, value in top_skills_of_years.items():
    make_inverted_hist(value, f'Топ-10 навыков по кол-ву упоминаний за {key} год\n для профессии {prof}', f'top_skills_{key}')

ensure_ascii = True

with open('stats/year_salary_dynamics.json', 'w') as file:
    json.dump(year_salary_dynamics, file, ensure_ascii=ensure_ascii, indent=4)

with open('stats/num_of_vacancies_per_year.json', 'w') as file:
    json.dump(num_of_vacancies_per_year, file, ensure_ascii=ensure_ascii, indent=4)

with open('stats/year_salary_dynamics_for_prof.json', 'w') as file:
    json.dump(year_salary_dynamics_for_prof, file, ensure_ascii=ensure_ascii, indent=4)

with open('stats/num_of_vacancies_per_year_for_prof.json', 'w') as file:
    json.dump(num_of_vacancies_per_year_for_prof, file, ensure_ascii=ensure_ascii, indent=4)

with open('stats/salary_levels_of_areas.json', 'w') as file:
    json.dump(salary_levels_of_areas, file, ensure_ascii=ensure_ascii, indent=4)

for key in vacancy_fractions_of_areas.keys():
    vacancy_fractions_of_areas[key] = "{:.2%}".format(float(vacancy_fractions_of_areas[key]))
with open('stats/vacancy_fractions_of_areas.json', 'w') as file:
    json.dump(vacancy_fractions_of_areas, file, ensure_ascii=ensure_ascii, indent=4)

with open('stats/top_skills_total.json', 'w') as file:
    json.dump(top_skills_total, file, ensure_ascii=ensure_ascii, indent=4)

with open('stats/top_skills_of_years.json', 'w') as file:
    json.dump(top_skills_of_years, file, ensure_ascii=ensure_ascii, indent=4)
