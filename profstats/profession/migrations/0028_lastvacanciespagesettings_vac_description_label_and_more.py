# Generated by Django 4.1.4 on 2023-01-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profession', '0027_remove_lastvacanciespagesettings_vac_description_label_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastvacanciespagesettings',
            name='vac_description_label',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='lastvacanciespagesettings',
            name='vac_name_label',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]