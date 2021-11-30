# Generated by Django 3.1 on 2020-12-09 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eshop_order', '0001_initial'),
        ('eshop_attribute', '0001_initial'),
        ('eshop_product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(verbose_name='امتیاز')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_attribute.attrproduct', verbose_name='ویژگی')),
            ],
            options={
                'verbose_name': 'امتیاز',
                'verbose_name_plural': 'امتیازات',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50, verbose_name='موضوع')),
                ('advantage', models.TextField(blank=True, null=True, verbose_name='نقاط قوت')),
                ('disadvantage', models.TextField(blank=True, null=True, verbose_name='نقاط ضعف')),
                ('comment', models.CharField(blank=True, max_length=250, verbose_name='نظر')),
                ('advice', models.CharField(choices=[('yes', 'خرید این محصول را پیشنهاد می\u200cکنم'), ('no', 'خرید این محصول را پیشنهاد نمی\u200cکنم'), ('omm', 'در مورد خرید این محصول نظری ندارم')], default='omm', max_length=100, verbose_name='توصیه')),
                ('affective_count', models.BigIntegerField(default='0', verbose_name='تعداد کامنت مفید')),
                ('notaffective_count', models.BigIntegerField(default='0', verbose_name='تعداد کامنت غیرمفید')),
                ('ip', models.CharField(blank=True, max_length=20, verbose_name='آی\u200cپی')),
                ('status', models.CharField(choices=[('New', 'در انتظار تائید'), ('Submit', 'تائید شده'), ('Not_submit', 'تائید نشده')], default='Submit', max_length=10, verbose_name='وضعیت')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='ایجاده شده در')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='آخرین آپدیت')),
                ('affective', models.ManyToManyField(blank=True, default=None, related_name='affective', to=settings.AUTH_USER_MODEL, verbose_name='کامنت مفید')),
                ('notaffective', models.ManyToManyField(blank=True, default=None, related_name='notaffective', to=settings.AUTH_USER_MODEL, verbose_name='کامنت غیرمفید')),
                ('order_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eshop_order.orderproduct', verbose_name='مدل محصول')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_product.product', verbose_name='نام محصول')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL, verbose_name='آیدی کاربر')),
            ],
            options={
                'verbose_name': 'نظرات مشتریان',
                'verbose_name_plural': 'نظرات مشتریان',
            },
        ),
    ]
