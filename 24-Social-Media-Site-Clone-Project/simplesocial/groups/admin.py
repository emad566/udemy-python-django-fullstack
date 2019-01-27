from django.contrib import admin
from .models import Group, GroupMemper
# Register your models here.

class GroupMemperInLine(admin.TabularInline):
    model = GroupMemper

admin.site.register(Group)

