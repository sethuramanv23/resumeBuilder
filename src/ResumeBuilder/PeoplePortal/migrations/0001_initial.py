# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institute_name', models.CharField(max_length=300)),
                ('degree', models.CharField(max_length=300)),
                ('degree_level', models.CharField(default=b'UG', max_length=30, choices=[(b'HSC', b'HSC'), (b'UG', b'UG'), (b'PG', b'PG'), (b'PHD', b'PHD'), (b'OTHER', b'OTHER')])),
                ('percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateTimeField(verbose_name=b'Date Published')),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
                ('email_id', models.EmailField(max_length=254)),
                ('career_objective', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='user',
            field=models.ForeignKey(to='PeoplePortal.User'),
        ),
    ]
