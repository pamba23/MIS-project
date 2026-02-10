from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import StudentProfile

@login_required
def student_dashboard(request):
    student = StudentProfile.objects.get(user=request.user)

    context = {
        "student": student
    }
    return render(request, "students_dashboard.html", context)
