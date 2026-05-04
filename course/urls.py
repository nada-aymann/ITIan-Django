from django.urls import path
from course.views import *

urlpatterns = [
    path('', courseList, name='CourseList'),
    path('add/', addCourse, name='AddCourse'),
    path('update/<int:id>/', updateCourse, name='UpdateCourse'),
    path('delete/<int:id>/', deleteCourse, name='DeleteCourse'),
]