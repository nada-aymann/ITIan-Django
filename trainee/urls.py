from django.urls import path, include
from trainee.views import *

urlpatterns = [
    path('api/', include('trainee.api.urls')),
    path('', TraineeListGeneric.as_view(), name='TraineeList'),
    path('<int:id>/', traineeDetails, name='TraineeDetails'),
    path('add/', AddTraineeGeneric.as_view(), name='AddTrainee'),
    path('update/<int:id>/', updateTrainee, name='UpdateTrainee'),
    path('delete/<int:id>/', deleteTrainee, name='DeleteTrainee'),
    ]   