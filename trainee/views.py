from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def traineeList(request):
    return render(request, 'trainee/list.html', {'trainees': Trainee.objects.all()})
def addTrainee(request):
    if request.method == 'POST':
        Trainee.objects.create(
            name = request.POST['trainee-name'],
            email = request.POST['trainee-email'],
            phone_number = request.POST['trainee-phone'],
            age = request.POST['trainee-age']
        )
        return redirect('TraineeList')
    return render(request, 'trainee/add_trainee.html')
def updateTrainee(request, id):
    return HttpResponse(f'<h1>Update trainee number:{id}</h1>')
def deleteTrainee(request, id):
    return HttpResponse(f'<h1>Delete trainee number:{id}</h1>')