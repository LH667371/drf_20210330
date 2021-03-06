# Generated by Django 2.2.19 on 2021-03-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='账号')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('birthday', models.DateField(verbose_name='生日')),
                ('gender', models.SmallIntegerField(choices=[(0, '男'), (1, '女'), (2, '未知')], default=2, verbose_name='性别')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号')),
                ('pic', models.ImageField(default='pic/1.jpg', upload_to='pic', verbose_name='头像')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
                'db_table': 'student_info',
            },
        ),
    ]
