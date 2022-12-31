# Generated by Django 4.1.4 on 2022-12-31 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profession', '0007_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='is_logo_changed',
            field=models.BooleanField(default=True, verbose_name='Заменить логотип'),
        ),
        migrations.AlterField(
            model_name='header',
            name='logo',
            field=models.FileField(upload_to='logos', verbose_name='Альтернативный логотип'),
        ),
    ]
