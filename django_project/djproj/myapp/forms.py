
from django import forms
from .models import Student, Track 

class StudentForm(forms.ModelForm):
      class Meta:
          model = Student
          #fields = ('fname','lname','age','st_track')
          #OR
          fields = '__all__'


class TrackForm(forms.ModelForm):
      class Meta:
          model = Track
          fields = '__all__'




