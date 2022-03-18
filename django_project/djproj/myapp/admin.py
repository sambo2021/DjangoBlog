from re import search
from django.contrib import admin
from .models import Student, Track
# Register your models here.

class CustomStudent(admin.ModelAdmin):
    fieldsets=(
         ['Student Info',{'fields':['fname','lname','age']}],
         ['Scholarship info',{'fields':['st_track']}]

    )
    list_display = ('fname','lname','age','st_track','is_adult')
    search_fields = ('fname','lname','st_track__track_name')
    list_filter = ('age','st_track__track_name')


class InlineStudent(admin.StackedInline):
    model = Student
    extra = 1 

class CustomTrack(admin.ModelAdmin):
    inlines =[InlineStudent]


admin.site.register(Student,CustomStudent)
admin.site.register(Track,CustomTrack)