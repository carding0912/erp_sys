# Generated by Django 3.2.6 on 2023-03-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0004_suppliermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creat_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='客户名称')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号码')),
                ('phone', models.CharField(blank=True, max_length=22, null=True, verbose_name='联系电话')),
                ('contacts_name', models.CharField(blank=True, max_length=22, null=True, verbose_name='联系人名')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='电子邮箱')),
                ('ratepayer_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='纳税人识别号码')),
                ('bank', models.CharField(blank=True, max_length=50, null=True, verbose_name='开户银行')),
                ('account_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='银行账号')),
                ('nation', models.CharField(blank=True, max_length=50, null=True, verbose_name='国家')),
                ('province', models.CharField(blank=True, max_length=50, null=True, verbose_name='省份')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='城市')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='详细地址')),
                ('remark', models.CharField(blank=True, max_length=512, null=True, verbose_name='备注')),
                ('init_receivable', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='初期应收')),
                ('current_receivable', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='末期应收')),
                ('order_number', models.IntegerField(default=100, verbose_name='排序号码')),
            ],
            options={
                'verbose_name': '客户',
                'verbose_name_plural': '客户',
                'db_table': 't_customer',
                'ordering': ['order_number', 'id'],
            },
        ),
    ]
