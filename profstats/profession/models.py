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

