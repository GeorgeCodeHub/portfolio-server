# Generated by Django 4.0.4 on 2022-05-27 14:04

import api.tools
from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('dateAcquired', models.DateField()),
            ],
            options={
                'db_table': 'certificates',
            },
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('dateFrom', models.DateField()),
                ('dateTo', models.DateField()),
            ],
            options={
                'db_table': 'degrees',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('positionTitle', models.CharField(max_length=100)),
                ('companyTitle', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('dateFrom', models.DateField()),
                ('dateTo', models.DateField()),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('isFeatured', models.BooleanField(null=True)),
                ('description', models.TextField()),
                ('githubURL', models.TextField(null=True)),
                ('runningAppURL', models.TextField(null=True)),
                ('technologies', api.tools.ChoiceArrayField(base_field=models.CharField(choices=[('C#', 'C#'), ('Django', 'Django'), ('ExpressJS', 'ExpressJS'), ('FastAPI', 'FastAPI'), ('Firebase', 'Firebase'), ('Javascript', 'Javascript'), ('PostgreSQL', 'PostgreSQL'), ('Python', 'Python'), ('ReactJS', 'ReactJS'), ('Tensorflow', 'Tensorflow'), ('Typescript', 'Typescript'), ('Unity3D', 'Unity3D')], max_length=100), default=list, size=None)),
                ('images', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
            ],
            options={
                'db_table': 'projects',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('technologies', api.tools.ChoiceArrayField(base_field=models.CharField(choices=[('C#', 'C#'), ('Django', 'Django'), ('ExpressJS', 'ExpressJS'), ('FastAPI', 'FastAPI'), ('Firebase', 'Firebase'), ('Javascript', 'Javascript'), ('PostgreSQL', 'PostgreSQL'), ('Python', 'Python'), ('ReactJS', 'ReactJS'), ('Tensorflow', 'Tensorflow'), ('Typescript', 'Typescript'), ('Unity3D', 'Unity3D')], max_length=100), default=list, size=None)),
            ],
            options={
                'db_table': 'skills',
            },
        ),
    ]
