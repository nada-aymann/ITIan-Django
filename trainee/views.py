from django.http import HttpResponse
from django.shortcuts import redirect, render
from course.models import Course
from trainee.forms import *
from .models import *


# Create your views here.

def traineeList(request):
    return render(request, 'trainee/list.html', {'trainees': Trainee.objects.all()})

def traineeDetails(request, id):
    trainee = Trainee.objects.get(id=id)
    return render(request, 'trainee/details.html', {'trainee': trainee})

def addTrainee(request):
    if request.method == 'POST':
        ###^ using ModelForm ### 
        form = TraineeFormModel(data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('TraineeList')
        

        ###? using django forms ###    
        # form = TraineeForm(data = request.POST)
        # if form.is_valid():
        #     Trainee.objects.create(
        #         name=request.POST['name'],
        #         email=request.POST['email'],
        #         phone_number=request.POST['phone_number'],
        #         age=request.POST['age'],
        #         course=Course.objects.get(pk=request.POST['course'])
        #     )
        #     return redirect('TraineeList')
        
    else:
        form = TraineeFormModel()
    return render(request, 'trainee/add_trainee.html', {'form': form})


def updateTrainee(request, id):
    trainee = Trainee.objects.get(id=id)
    courses = Course.objects.all()
    if request.method == 'POST':
        trainee.name = request.POST['trainee-name']
        trainee.email = request.POST['trainee-email']
        trainee.phone_number = request.POST['trainee-phone']
        trainee.age = request.POST['trainee-age']
        if 'trainee-image' in request.FILES:
            trainee.image = request.FILES['trainee-image']
        trainee.course = Course.objects.get(pk=request.POST['trainee-course'])
        trainee.save()
        return redirect('TraineeList')
    return render(request, 'trainee/update.html', {'trainee': trainee, 'courses': courses})

def deleteTrainee(request, id):
    trainee = Trainee.objects.get(id=id)
    
    if request.method == 'POST':
        trainee.delete()
        return redirect('TraineeList')

    return render(request, 'trainee/delete.html', {'trainee': trainee})