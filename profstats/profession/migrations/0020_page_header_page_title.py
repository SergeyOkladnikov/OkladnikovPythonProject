# Generated by Django 4.1.4 on 2023-01-08 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profession', '0019_delete_homesettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='header',
            field=models.CharField(blank=True, max_length=100, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(blank=True, max_length=50, verbose_name='Заголовок вкладки'),
        ),
    ]
