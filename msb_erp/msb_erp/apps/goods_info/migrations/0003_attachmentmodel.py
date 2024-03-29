# Generated by Django 3.2.6 on 2023-03-20 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods_info', '0002_unitsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creat_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('a_file', models.FileField(upload_to='', verbose_name='附件或者图片')),
                ('a_type', models.CharField(blank=True, choices=[('image', '图片'), ('doc', 'Word文档'), ('excel', 'Excel文档'), ('zip', '压缩文件'), ('other', '其他文件')], max_length=20, null=True, verbose_name='附件的类型')),
            ],
            options={
                'verbose_name': '附件表',
                'verbose_name_plural': '附件表',
                'db_table': 't_attachment',
                'ordering': ['id'],
            },
        ),
    ]
