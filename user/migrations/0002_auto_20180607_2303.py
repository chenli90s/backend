# Generated by Django 2.0.3 on 2018-06-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='预告信息')),
                ('date_time', models.DateTimeField(blank=True, null=True, verbose_name='预告时间')),
            ],
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': '信息'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': '账号'},
        ),
        migrations.AlterField(
            model_name='news',
            name='auth',
            field=models.ForeignKey(on_delete=None, to='user.User', verbose_name='发布者'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_content',
            field=models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_count',
            field=models.TextField(blank=True, default=None, max_length=11, null=True, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_dt',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_phone',
            field=models.TextField(blank=True, default=None, max_length=11, null=True, verbose_name='联系电话'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_price',
            field=models.TextField(blank=True, default=None, max_length=12, null=True, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_title',
            field=models.TextField(blank=True, default=None, max_length=50, null=True, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_addr',
            field=models.TextField(blank=True, default=None, max_length=50, null=True, verbose_name='用户地址'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.TextField(blank=True, default=None, max_length=50, null=True, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_num',
            field=models.TextField(blank=True, default=None, max_length=50, null=True, verbose_name='用户编号'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_pass',
            field=models.TextField(blank=True, default=None, max_length=50, null=True, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_phone',
            field=models.TextField(blank=True, default=None, max_length=50, null=True, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_real',
            field=models.TextField(blank=True, default=None, max_length=50, null=True, verbose_name='实名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.TextField(blank=True, default=None, max_length=50, null=True, verbose_name='角色'),
        ),
    ]
