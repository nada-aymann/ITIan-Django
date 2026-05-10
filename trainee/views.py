from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def traineeList(request):
    return render(request, 'trainee/list.html', {'trainees': Trainee.objects.all()})

def traineeDetails(request, id):
    trainee = Trainee.objects.get(id=id)
    return render(request, 'trainee/details.html', {'trainee': trainee})

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
    trainee = Trainee.objects.get(id=id)
    if request.method == 'POST':
        trainee.name = request.POST['trainee-name']
        trainee.email = request.POST['trainee-email']
        trainee.phone_number = request.POST['trainee-phone']
        trainee.age = request.POST['trainee-age']
        trainee.save()
        return redirect('TraineeList')
    return render(request, 'trainee/update.html', {'trainee': trainee})

def deleteTrainee(request, id):
    trainee = Trainee.objects.get(id=id)
    
    if request.method == 'POST':
        trainee.delete()
        return redirect('TraineeList')

    return render(request, 'trainee/delete.html', {'trainee': trainee})