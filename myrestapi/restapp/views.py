from .models import AllSubject, Attendance, BookDistribution, Class, ClassSubjects, Library, Students, Teachers, TeacherSubject, Profile

from .serializers import AllSubjectSerializer, AttendanceSerializer, BookDistributionSerializer, ClassSerializer, ClassSubjectSerializer, LibrarySerializer, RegistrationSerializer, TeachersSerializer, TeacherSubjectSerializer, ProfileSerializer, StudentsSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from .permissions import IsTeacher, ReadOnly, IsLibrarian, IsStudent
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class QuickLinks(APIView):
    """
    Only Quicklinks and Allsubjects Apis made with APIView and Others made with generic views
    And User Profiles create automatically(use of signals) when user register
    """
    def get(self, request, format=None):
        return Response({
        'students': reverse('students', request=request, format=format),
        'teachers': reverse('teachers', request=request, format=format),
        'allsubjects': reverse('allsubjects', request=request, format=format),
        'attendance': reverse('attendance', request=request, format=format),
        'bookdistribution': reverse('bookdistribution', request=request, format=format),
        'class': reverse('class', request=request, format=format),
        'classsubjects': reverse('classsubjects', request=request, format=format),
        'library': reverse('library', request=request, format=format),
        'registration': reverse('registration', request=request, format=format),
        'allregistrations':  reverse('allregistrations', request=request, format=format),
        'teachersubjects': reverse('teachersubjects', request=request, format=format),
        'profile': reverse('profile', request=request, format=format),
        })

class StudentsView(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsTeacher|IsAdminUser]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filter_fields = ['student_name', 'class_field', 'admission_year', 'roll_number']
    ordering_fields = ['student_name']
    search_fields = ['student_name', 'father_name']

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    lookup_field = 'student_name'
    permission_classes = [IsTeacher|IsAdminUser]

class AllSubjectView(APIView):
    permission_classes = [IsTeacher|IsAdminUser|ReadOnly]
    def get(self, request, format=None):
        allsubjects = AllSubject.objects.all()
        serializer = AllSubjectSerializer(allsubjects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AllSubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttendanceView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsTeacher|IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['class_field', 'date_of_attendance', 'attendance_status', 'student_name']

class BookDistributionView(generics.ListCreateAPIView):
    queryset = BookDistribution.objects.all()
    serializer_class = BookDistributionSerializer
    permission_classes = [IsLibrarian|IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'

class ClassView(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAdminUser|IsTeacher|ReadOnly]

class ClassSubjectsView(generics.ListCreateAPIView):
    queryset = ClassSubjects.objects.all()
    serializer_class = ClassSubjectSerializer
    permission_classes = [IsAdminUser|IsTeacher|ReadOnly]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['class_name', 'subjects']

class LibraryView(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsLibrarian|IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['book_name', 'class_field']

class AllRegistrationsView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['username', 'groups']

class SingleRegistrationView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    lookup_field = 'username'
    permission_classes = [IsAdminUser]

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

class TeachersView(generics.ListCreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    permission_classes = [IsAdminUser|IsTeacher|ReadOnly]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['teacher_name', 'class_teacher']

class SingleTeacherView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    lookup_field = 'teacher_name'
    permission_classes = [IsAdminUser|IsTeacher|ReadOnly]

class TeacherSubjectView(generics.ListCreateAPIView):
    queryset = TeacherSubject.objects.all()
    serializer_class = TeacherSubjectSerializer
    permission_classes = [IsAdminUser|IsTeacher|ReadOnly]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['teacher_name']

class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]