from django.contrib import admin
from App.models import Student;
# Register your models here.
class StudentTable(admin.ModelAdmin):
    list_display=('name','mark')
admin.site.register(Student,StudentTable)
