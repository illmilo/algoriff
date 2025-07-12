from django.shortcuts import render

# importing models from other app
from home.models import Courses

# Create your views here.
def courses(request):
    courses = Courses.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses/courses.html', context)
