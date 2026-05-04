from django.urls import path
from trainee.views import *

urlpatterns = [
    path('', traineeList, name='TraineeList'),
    path('add/', addTrainee, name='AddTrainee'),
    path('update/<int:id>/', updateTrainee, name='UpdateTrainee'),
    path('delete/<int:id>/', deleteTrainee, name='DeleteTrainee'),
    ]