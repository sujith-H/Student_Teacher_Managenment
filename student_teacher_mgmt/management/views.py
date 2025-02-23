from django.views.generic import ListView, DetailView
from .models import Teacher, Student

class TeacherListView(ListView):
    model = Teacher
    template_name = "teacher_list.html"  # Create this template

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = "teacher_detail.html"  # Create this template

class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"  # Create this template

class StudentDetailView(DetailView):
    model = Student
    template_name = "student_detail.html"  # Create this template
