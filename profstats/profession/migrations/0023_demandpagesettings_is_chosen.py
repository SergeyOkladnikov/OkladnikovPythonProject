# Generated by Django 4.1.4 on 2023-01-08 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profession', '0022_alter_demandpagesettings_comparison_graphs_header_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandpagesettings',
            name='is_chosen',
            field=models.BooleanField(default=True),
        ),
    ]