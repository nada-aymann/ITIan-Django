from django.urls import path, include
from course.views import *

urlpatterns = [
    path('api/', include('course.api.urls')),
    path('', courseList, name='CourseList'),
    path('<int:id>/', courseDetails, name='CourseDetails'),
    path('add/', addCourse, name='AddCourse'),
    path('update/<int:id>/', updateCourse, name='UpdateCourse'),
    path('delete/<int:id>/', deleteCourse, name='DeleteCourse'),
]