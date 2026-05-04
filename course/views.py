from django.http import HttpResponse
from django.shortcuts import render


def courseList(request):
    courses = [
        {'id': 1, 'title': 'Front-End Development'},
        {'id': 2, 'title': 'Back-End Development'},
        {'id': 3, 'title': 'Full-Stack Development'},
    ]
    return render(request, 'course/list.html', {'courses': courses})
def addCourse(request):
    return render(request, 'course/add_course.html')
def updateCourse(request, id):
    return HttpResponse(f'<h1>Update course number:{id}</h1>')
def deleteCourse(request, id):
    return HttpResponse(f'<h1>Delete course number:{id}</h1>')