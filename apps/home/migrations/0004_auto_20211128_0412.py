# Generated by Django 3.2.9 on 2021-11-28 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20211128_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='exitDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='size',
            field=models.FloatField(blank=True, null=True),
        ),
    ]