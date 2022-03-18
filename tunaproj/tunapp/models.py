from django.db import models

# Create your models here.
# Create your models here.
class Track(models.Model):
    track_name = models.CharField(max_length=20)
    def __str__(self):
        return self.track_name

class Student(models.Model):
    fname = models.CharField(max_length=50, null=True)
    lname = models.CharField(max_length=50, null=True)
    age = models.IntegerField()
    student_track = models.ForeignKey(Track, on_delete=models.CASCADE)
    def __str__(self):
        return self.fname + ' ' + self.lname

    def is_graduate(self):
        if(self.age >= 10):
            return True
        else:
            return False
    is_graduate.boolean = True
    is_graduate.short_description = 'post graduated'