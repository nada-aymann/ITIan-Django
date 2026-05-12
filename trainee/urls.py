from django.urls import path
from trainee.views import *

urlpatterns = [
    path('', TraineeListGeneric.as_view(), name='TraineeList'),
    path('<int:id>/', traineeDetails, name='TraineeDetails'),
    path('add/', AddTraineeGeneric.as_view(), name='AddTrainee'),
    path('update/<int:id>/', updateTrainee, name='UpdateTrainee'),
    path('delete/<int:id>/', deleteTrainee, name='DeleteTrainee'),
    ]   