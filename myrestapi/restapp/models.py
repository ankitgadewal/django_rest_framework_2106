from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

attendance_status = (('Present', 'Present'), ('Absent', 'Absent'))

class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.class_name

class Students(models.Model):
    student_name = models.CharField(unique=True, max_length=50)
    father_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='study_in')
    roll_number = models.IntegerField()
    admission_year = models.IntegerField()
    dob = models.DateField()

    def __str__(self):
        return self.student_name

class AllSubject(models.Model):
    name_of_subject = models.CharField(max_length=50)

    def __str__(self):
        return self.name_of_subject

class Attendance(models.Model):
    date_of_attendance = models.DateTimeField(default=timezone.now)
    student_name = models.ForeignKey(Students, on_delete=models.CASCADE)
    attendance_status = models.CharField(max_length=7, choices=attendance_status)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student_name)

class Library(models.Model):
    book_name = models.CharField(max_length=50)
    book_author = models.CharField(max_length=30)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE)
    no_of_copies = models.IntegerField()

    def __str__(self):
        return self.book_name

class BookDistribution(models.Model):
    book_name = models.ForeignKey(Library, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Students, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.book_name)

class ClassSubjects(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    subjects = models.ForeignKey(AllSubject, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.class_name) + ' subject ' + str(self.subjects)

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)
        
class Teachers(models.Model):
    teacher_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    class_teacher = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name

class TeacherSubject(models.Model):
    teacher_name = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    teaching_subject = models.ForeignKey(AllSubject, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.teacher_name)
