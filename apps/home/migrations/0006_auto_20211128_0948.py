# Generated by Django 3.2.9 on 2021-11-28 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_remove_asset_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asset',
            name='exitDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='orderDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
