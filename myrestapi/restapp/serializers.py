from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from .models import (AllSubject, Attendance, BookDistribution, Class, ClassSubjects, Library, 
    Students, Teachers, TeacherSubject, Profile, MyUploads)

class StudentsSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='single-student', format='html', lookup_field='student_name')
    class Meta:
        model = Students
        fields = ['url', 'student_name', 'father_name', 'mobile_number', 'class_field', 'roll_number', 'admission_year', 'dob']

class TeachersSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='single-teacher',lookup_field='teacher_name', format='html')
    class Meta:
        model = Teachers
        fields = ['url', 'teacher_name', 'mobile_number', 'class_teacher']


class RegistrationSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='singleuser', format='html', lookup_field='username')
    password = serializers.CharField(
        write_only=True,
        help_text='Choose a Strong Password',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'groups']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(RegistrationSerializer, self).create(validated_data)


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['date_of_attendance', 'student_name', 'attendance_status', 'class_field']

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class AllSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllSubject
        fields = '__all__'

class ClassSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassSubjects
        fields = ['class_name', 'subjects']

class TeacherSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSubject
        fields = '__all__'

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['book_name', 'book_author', 'class_field', 'no_of_copies']

class BookDistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDistribution
        fields = '__all__'

class MyUploadsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = MyUploads
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name='SingleProfile', format='html', lookup_field='pk')
    class Meta:
        model = Profile
        fields = ['owner', 'url', 'profile_pic', 'hobby', 'address', 'username']