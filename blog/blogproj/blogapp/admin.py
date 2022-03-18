from django.contrib import admin
from .models import Student, Track
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Student Info', {'fields': ['fname', 'lname', 'age']}],
        ['Scholarship Info', {'fields': ['student_track']}],

    )
    list_display = ('fname','lname','age','student_track','is_graduate')
    list_filter = ['fname', 'age','student_track']
    search_fields = ['fname', 'age', 'student_track__track_name']

class InlineStudent(admin.StackedInline):
    model = Student
    extra = 2

class TrackAdmin(admin.ModelAdmin):
    inlines=[InlineStudent]


admin.site.register(Student, StudentAdmin)
admin.site.register(Track, TrackAdmin)




