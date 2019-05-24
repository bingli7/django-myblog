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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='标题', max_length=200)),
                ('content', models.TextField(verbose_name='内容', default='blog content')),
                ('pub_date', models.DateTimeField(verbose_name='发表时间', auto_now=True)),
            ],
        ),
    ]
