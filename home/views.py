from django.shortcuts import render

from .models import Courses, PublicRelations

# Create your views here.
def home(request):
    popular_courses = Courses.objects.all()
    pros = PublicRelations.objects.all()
    context = {
        'popular_courses': popular_courses,
        'pros': pros,
    }
    return render(request, 'home/home.html', context)
