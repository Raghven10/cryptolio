# Generated by Django 3.2.9 on 2021-11-08 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderDate', models.DateTimeField()),
                ('exchange', models.CharField(max_length=20)),
                ('token', models.CharField(max_length=20)),
                ('tradeType', models.CharField(max_length=20)),
                ('leverage', models.IntegerField()),
                ('entryPrice', models.FloatField()),
                ('totalQuantity', models.FloatField()),
                ('exitPrice', models.FloatField()),
                ('lastUpdatedOn', models.DateTimeField()),
                ('lastUpdatedBy', models.CharField(max_length=20)),
            ],
        ),
    ]
