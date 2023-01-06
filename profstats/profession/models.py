from django.db import models


class NavElement(models.Model):
    label = models.CharField(max_length=25, verbose_name='Название')
    url_name = models.CharField(max_length=100, verbose_name='Имя URL')

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = 'Элемент навигации'
        verbose_name_plural = 'Элементы навигации'


class FooterElement(models.Model):
    label = models.CharField(max_length=25, verbose_name='Название', blank=True)
    content = models.CharField(max_length=100, verbose_name='Содержание')

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = 'Элемент подвала'
        verbose_name_plural = 'Элементы подвала'


class Header(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    logo = models.FileField(upload_to='logos', verbose_name='Альтернативный логотип')
    is_logo_changed = models.BooleanField(default=True, verbose_name='Заменить логотип')
    is_logo_shown = models.BooleanField(default=True, verbose_name='Отображать логотип')
    is_prof_name_shown = models.BooleanField(default=True, verbose_name='Отображать название профессии')
    is_chosen = models.BooleanField(default=False, verbose_name='Выбран')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вариант шапки'
        verbose_name_plural = 'Варианты шапки'


class Profession(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название профессии')
    text_block_1 = models.TextField(verbose_name='Блок текста 1', blank=True)
    image_1 = models.ImageField(upload_to='photos/', verbose_name='Изображение 1', blank=True)
    image_1_caption = models.CharField(max_length=100, verbose_name='Подпись изображения 1', blank=True)
    text_block_2 = models.TextField(verbose_name='Блок текста 2', blank=True)
    image_2 = models.ImageField(upload_to='photos/', verbose_name='Изображение 2', blank=True)
    image_2_caption = models.CharField(max_length=100, verbose_name='Подпись изображения 2', blank=True)
    text_block_3 = models.TextField(verbose_name='Блок текста 3', blank=True)
    image_3 = models.ImageField(upload_to='photos/', verbose_name='Изображение 3', blank=True)
    image_3_caption = models.CharField(max_length=100, verbose_name='Подпись изображения 3', blank=True)

    years_stats = models.FileField(upload_to='stats/', blank=True, verbose_name='Статистика по годам')

    years_salary_graph = models.FileField(upload_to='graphs/years', blank=True, verbose_name='График: Динамика уровня зарплат по годам')
    years_vac_num_graph = models.FileField(upload_to='graphs/years', blank=True, verbose_name='График: Динамика количества вакансий по годам')
    years_salary_for_prof_graph = models.FileField(upload_to='graphs/years', blank=True, verbose_name='График: Динамика уровня зарплат по годам для выбранной профессии')
    years_vac_num_for_prof_graph = models.FileField(upload_to='graphs/years', blank=True, verbose_name='График: Динамика количества вакансий по годам для выбранной профессии')

    years_salary_comparison_graph = models.FileField(upload_to='graphs/years', blank=True, verbose_name='График: Динамика уровня зарплат по годам (сравнение)')
    years_vac_num_comparison_graph = models.FileField(upload_to='graphs/years', blank=True, verbose_name='График: Динамика количества вакансий по годам (сравнение)')

    areas_stats = models.FileField(upload_to='stats/', blank=True, verbose_name='Статистика по регионам')

    areas_salary_graph = models.FileField(upload_to='graphs/areas', blank=True, verbose_name='График: Уровень зарплат по городам')
    areas_vac_fractions_graph = models.FileField(upload_to='graphs/areas', blank=True, verbose_name='График: Доля вакансий по городам')

    skills_stats = models.FileField(upload_to='stats/', blank=True, verbose_name='Статистика по востребованности навыков')
    top_skills_total_graph = models.FileField(upload_to='graphs/skills', blank=True, verbose_name='График: Востребованность навыков за всё время')

    is_chosen = models.BooleanField(verbose_name='Выбрана', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

