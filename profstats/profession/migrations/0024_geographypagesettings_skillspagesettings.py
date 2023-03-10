# Generated by Django 4.1.4 on 2023-01-08 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profession', '0023_demandpagesettings_is_chosen'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeographyPageSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('graphs_block_header', models.CharField(blank=True, max_length=150)),
                ('tables_block_header', models.CharField(blank=True, max_length=150)),
                ('is_chosen', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkillsPageSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('graphs_block_header', models.CharField(blank=True, max_length=150)),
                ('graphs_block_one_header', models.CharField(blank=True, max_length=250)),
                ('graphs_block_two_header', models.CharField(blank=True, max_length=250)),
                ('tables_block_header', models.CharField(blank=True, max_length=150)),
                ('is_chosen', models.BooleanField(default=True)),
            ],
        ),
    ]
