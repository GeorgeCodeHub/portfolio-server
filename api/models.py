from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField

from api.tools import FUNCTION_CHOICES, ChoiceArrayField


class Certificate(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=100, null=False)
    school = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    dateAcquired = models.DateField(null=False)

    class Meta:
        db_table = "certificates"

    # define string representation for this model class, will be used when display model class data in django admin web site.
    def __str__(self):
        return self.title


class Degree(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=100, null=False)
    school = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    dateFrom = models.DateField(null=False)
    dateTo = models.DateField(null=False)

    class Meta:
        db_table = "degrees"

    # define string representation for this model class, will be used when display model class data in django admin web site.
    def __str__(self):
        return self.title


class Job(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    positionTitle = models.CharField(max_length=100, null=False)
    companyTitle = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    dateFrom = models.DateField(null=False)
    dateTo = models.DateField(null=False)

    class Meta:
        db_table = "jobs"

    # define string representation for this model class, will be used when display model class data in django admin web site.
    def __str__(self):
        return self.positionTitle


class Project(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=100, null=False)
    isFeatured = models.BooleanField(null=True)
    description = models.TextField(null=False)
    githubURL = models.TextField(null=True)
    runningAppURL = models.TextField(null=True)
    technologies = ChoiceArrayField(
        base_field=models.CharField(max_length=100, choices=FUNCTION_CHOICES),
        default=list,
        null=False,
    )
    images = ArrayField(models.CharField(max_length=100, null=False), null=False)

    class Meta:
        db_table = "projects"

    # define string representation for this model class, will be used when display model class data in django admin web site.
    def __str__(self):
        return self.title


class Skill(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=100, null=False)
    technologies = ChoiceArrayField(
        base_field=models.CharField(max_length=100, choices=FUNCTION_CHOICES),
        default=list,
        null=False,
    )

    class Meta:
        db_table = "skills"

    # define string representation for this model class, will be used when display model class data in django admin web site.
    def __str__(self):
        return self.title
