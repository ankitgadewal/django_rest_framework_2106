from django.contrib import admin
from .models import AllSubject, Attendance, BookDistribution, Class, ClassSubjects, Library, Students, Teachers, TeacherSubject, Profile

# Register your models here.
admin.site.register((AllSubject, Attendance, BookDistribution, Class, ClassSubjects, Library, Students, Teachers, TeacherSubject, Profile))

