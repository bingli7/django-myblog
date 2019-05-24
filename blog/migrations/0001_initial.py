# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=200)),
                ('content', models.TextField(default='Blog Content', verbose_name='内容')),
                ('pub_time', models.DateTimeField(verbose_name='发表日期', auto_now=True)),
            ],
        ),
    ]
