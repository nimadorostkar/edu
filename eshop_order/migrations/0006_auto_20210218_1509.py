# Generated by Django 3.1 on 2021-02-18 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_order', '0005_auto_20201229_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='eshop_order.order', verbose_name='سفارش'),
        ),
    ]
