from rest_framework import serializers
from .models import Student, Track

class StudentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student
        fields = ['id','fname', 'lname', 'age', 'student_track']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['track_name'] = instance.st_track.track_name
        return rep 

class TrackSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student
        fields = ['track_name']

    
