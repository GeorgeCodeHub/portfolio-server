from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

# Register your models here.
from .models import Email


class EmailAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "message", "dateSent"]


admin.site.register(Email, EmailAdmin)
