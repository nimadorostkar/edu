# Generated by Django 3.2.4 on 2021-06-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_variant', '0004_auto_20210202_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='size',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='variants',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]