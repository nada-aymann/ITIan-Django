from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def courseList(request):
    return render(request, 'course/list.html', {'courses': Course.objects.all()})

@login_required
def courseDetails(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'course/details.html', {'course': course})

@login_required
def addCourse(request):
    if request.method == 'POST':
        Course.objects.create(
            name = request.POST['course-name'],
            duration = request.POST['course-duration']
        )
        return redirect('CourseList')
    return render(request, 'course/add_course.html')

@login_required
def updateCourse(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        course.name = request.POST['course-name']
        course.duration = request.POST['course-duration']
        course.save()
        return redirect('CourseList')
    return render(request, 'course/update.html', {'course': course})

@login_required
def deleteCourse(request, id):
    course = Course.objects.get(id=id)

    if request.method == 'POST':
        course.delete()
        return redirect('CourseList')

    return render(request, 'course/delete.html', {'course': course})