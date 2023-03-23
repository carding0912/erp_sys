# Generated by Django 3.2.6 on 2023-03-20 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0007_settlementaccountmodel'),
        ('goods_info', '0003_attachmentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creat_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='货品名称')),
                ('specification', models.CharField(blank=True, max_length=50, null=True, verbose_name='规格')),
                ('model_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='型号')),
                ('color', models.CharField(blank=True, max_length=50, null=True, verbose_name='颜色')),
                ('basic_weight', models.CharField(blank=True, max_length=50, null=True, verbose_name='基础重量')),
                ('expiration_day', models.IntegerField(blank=True, null=True, verbose_name='保质期')),
                ('remark', models.CharField(blank=True, max_length=512, null=True, verbose_name='备注')),
                ('number_code', models.CharField(max_length=28, unique=True, verbose_name='编号或者批号')),
                ('purchase_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='采购价')),
                ('retail_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='零售价')),
                ('sales_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='销售价')),
                ('lowest_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='最低售价')),
                ('order_number', models.IntegerField(default=100, verbose_name='排序号码')),
                ('images_list', models.CharField(blank=True, max_length=20, null=True, verbose_name='商品图片所对应的id列表')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goods_info.goodscategorymodel')),
                ('units', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goods_info.unitsmodel')),
            ],
            options={
                'verbose_name': '货品表',
                'verbose_name_plural': '货品表',
                'db_table': 't_goods',
                'ordering': ['order_number', 'id'],
            },
        ),
        migrations.CreateModel(
            name='GoodsInventoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('init_inventory', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='期初库存数量')),
                ('cur_inventory', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='现在库存数量')),
                ('lowest_inventory', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='最低安全库存, 0表示不设置')),
                ('highest_inventory', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='最高安全库存,0表示不设置')),
                ('warehouse_name', models.CharField(max_length=50, verbose_name='仓库的名称')),
                ('goods', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inventory_list', to='goods_info.goodsmodel')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_info.warehousemodel')),
            ],
            options={
                'verbose_name': '货品库存表',
                'verbose_name_plural': '货品库存表',
                'db_table': 't_goods_inventory',
                'ordering': ['id'],
            },
        ),
    ]
