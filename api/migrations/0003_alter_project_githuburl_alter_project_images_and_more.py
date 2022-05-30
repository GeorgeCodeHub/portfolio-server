# Generated by Django 4.0.4 on 2022-05-30 21:31

import api.tools
from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_job_dateto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='githubURL',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='images',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=300), size=None),
        ),
        migrations.AlterField(
            model_name='project',
            name='runningAppURL',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=api.tools.ChoiceArrayField(base_field=models.CharField(choices=[('Blender3D', 'Blender3D'), ('CSS', 'CSS'), ('C#', 'C#'), ('Django', 'Django'), ('ExpressJS', 'ExpressJS'), ('FastAPI', 'FastAPI'), ('Firebase', 'Firebase'), ('HTML', 'HTML'), ('Javascript', 'Javascript'), ('Keras', 'Keras'), ('NextJS', 'NextJS'), ('NodeJS', 'NodeJS'), ('OpenCV', 'OpenCV'), ('PostgreSQL', 'PostgreSQL'), ('Python', 'Python'), ('ReactJS', 'ReactJS'), ('Tensorflow', 'Tensorflow'), ('Typescript', 'Typescript'), ('Unity3D', 'Unity3D')], max_length=100), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='skill',
            name='technologies',
            field=api.tools.ChoiceArrayField(base_field=models.CharField(choices=[('Blender3D', 'Blender3D'), ('CSS', 'CSS'), ('C#', 'C#'), ('Django', 'Django'), ('ExpressJS', 'ExpressJS'), ('FastAPI', 'FastAPI'), ('Firebase', 'Firebase'), ('HTML', 'HTML'), ('Javascript', 'Javascript'), ('Keras', 'Keras'), ('NextJS', 'NextJS'), ('NodeJS', 'NodeJS'), ('OpenCV', 'OpenCV'), ('PostgreSQL', 'PostgreSQL'), ('Python', 'Python'), ('ReactJS', 'ReactJS'), ('Tensorflow', 'Tensorflow'), ('Typescript', 'Typescript'), ('Unity3D', 'Unity3D')], max_length=100), default=list, size=None),
        ),
    ]
