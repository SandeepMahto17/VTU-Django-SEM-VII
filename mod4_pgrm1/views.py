from django.views.generic import ListView, DetailView
from .models import Student

# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = 'student_list_1.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'

