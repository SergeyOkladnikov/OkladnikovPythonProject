# Generated by Django 4.1.4 on 2023-01-08 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profession', '0021_demandpagesettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandpagesettings',
            name='comparison_graphs_header',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='demandpagesettings',
            name='graphs_block_header',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='demandpagesettings',
            name='one_var_graphs_header',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='demandpagesettings',
            name='tables_block_header',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
