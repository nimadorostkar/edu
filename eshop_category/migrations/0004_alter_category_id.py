# Generated by Django 3.2.4 on 2021-06-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_category', '0003_auto_20201214_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
