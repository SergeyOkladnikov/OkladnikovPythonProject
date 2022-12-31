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
