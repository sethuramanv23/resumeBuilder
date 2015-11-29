# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template_name', models.CharField(max_length=200)),
                ('template_body', models.TextField()),
                ('resume_format', models.CharField(default=b'PDF', max_length=30, choices=[(b'PDF', b'PDF')])),
                ('creation_date', models.DateTimeField(verbose_name=b'Date Published')),
            ],
        ),
    ]
