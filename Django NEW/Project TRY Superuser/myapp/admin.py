from django.contrib import admin
from . models import *

# Register your models here.

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display=['id','First_Name_P','Email_ID_P']

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display=['id','First_Name_C','Email_ID_C','Parent_ID']