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
    is_chosen = models.BooleanField(verbose_name='Выбрана', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


class Page(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название страницы')
    label = models.CharField(max_length=70, verbose_name='Отображаемое имя')
    title = models.CharField(max_length=50, verbose_name='Заголовок вкладки', blank=True)
    header = models.CharField(max_length=100, verbose_name='Заголовок страницы', blank=True)

    def __str__(self):
        return self.label


class NonProfConnectedGraph(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    label = models.CharField(max_length=150, verbose_name='Подпись', blank=True)
    graph = models.FileField(upload_to='graphs/demand', verbose_name='График')
    page = models.ForeignKey('Page', on_delete=models.PROTECT, verbose_name='Страница')
    is_shown = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'График, не связанный с профессией'
        verbose_name_plural = 'Графики, не связанные с профессией'


class ProfConnectedGraph(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    label = models.CharField(max_length=150, verbose_name='Подпись', blank=True)
    graph = models.FileField(upload_to='graphs/demand', verbose_name='График')
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, verbose_name='Профессия')
    page = models.ForeignKey('Page', on_delete=models.PROTECT, verbose_name='Страница')
    is_shown = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'График, связанный с профессией'
        verbose_name_plural = 'Графики, связанные с профессией'


class ComparisonGraph(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    label = models.CharField(max_length=150, verbose_name='Подпись', blank=True)
    graph = models.FileField(upload_to='graphs/demand', verbose_name='График')
    page = models.ForeignKey('Page', on_delete=models.PROTECT, verbose_name='Страница')
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, verbose_name='Профессия')
    is_shown = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'График  сравнительный'
        verbose_name_plural = 'Графики сравнительные'


class NonProfConnectedTableData(models.Model):
    label = models.CharField(max_length=250, verbose_name='Название')
    keys_label = models.CharField(max_length=50, verbose_name='Название левого столбца')
    values_label = models.CharField(max_length=50, verbose_name='Название правого столбца')
    data = models.FileField(upload_to='stat_data/', verbose_name='Данные')
    max_rows = models.IntegerField(verbose_name='Максимальное кол-во строк', default=15)
    page = models.ForeignKey('Page', on_delete=models.PROTECT, verbose_name='Страница')
    is_shown = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = 'Таблица, не связанная с профессией'
        verbose_name_plural = 'Таблицы, не связанные с профессией'


class ProfConnectedTableData(models.Model):
    label = models.CharField(max_length=250, verbose_name='Название')
    keys_label = models.CharField(max_length=50, verbose_name='Название левого столбца')
    values_label = models.CharField(max_length=50, verbose_name='Название правого столбца')
    data = models.FileField(upload_to='stat_data/', verbose_name='Данные')
    max_rows = models.IntegerField(verbose_name='Максимальное кол-во строк', default=15)
    page = models.ForeignKey('Page', on_delete=models.PROTECT, verbose_name='Страница')
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, verbose_name='Профессия')
    is_shown = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = 'Таблица, связанная с профессией'
        verbose_name_plural = 'Таблицы, связанные с профессией'


class TableSeriesData(models.Model):
    label = models.CharField(max_length=250, verbose_name='Название')
    keys_label = models.CharField(max_length=50, verbose_name='Название левого столбца')
    values_label = models.CharField(max_length=50, verbose_name='Название правого столбца')
    data = models.FileField(upload_to='stat_data/', verbose_name='Данные')
    max_rows = models.IntegerField(verbose_name='Максимальное кол-во строк для одной таблицы', default=10)
    page = models.ForeignKey('Page', on_delete=models.PROTECT, verbose_name='Страница')
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, verbose_name='Профессия', null=True)
    is_shown = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = 'Группа таблиц, содержащих различные варианты одного признака'
        verbose_name_plural = 'Группы таблиц, содержащих различные варианты одного признака'


class DemandPageSettings(models.Model):
    name = models.CharField(max_length=150)
    graphs_block_header = models.CharField(max_length=150, blank=True)
    one_var_graphs_header = models.CharField(max_length=250, blank=True)
    comparison_graphs_header = models.CharField(max_length=250, blank=True)
    tables_block_header = models.CharField(max_length=150, blank=True)
    is_chosen = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class GeographyPageSettings(models.Model):
    name = models.CharField(max_length=150)
    graphs_block_header = models.CharField(max_length=150, blank=True)
    tables_block_header = models.CharField(max_length=150, blank=True)
    is_chosen = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SkillsPageSettings(models.Model):
    name = models.CharField(max_length=150)
    graphs_block_header = models.CharField(max_length=150, blank=True)
    graphs_block_one_header = models.CharField(max_length=250, blank=True)
    graphs_block_two_header = models.CharField(max_length=250, blank=True)
    tables_block_header = models.CharField(max_length=150, blank=True)
    is_chosen = models.BooleanField(default=True)

    def __str__(self):
        return self.name

