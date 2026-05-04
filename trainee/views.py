from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def traineeList(request):
    trainees = [
        {"id": 1, "name": "Nada Ayman"},
        {"id": 2, "name": "Ahmed Ali"},
        {"id": 3, "name": "Sara Mohamed"},
    ]
    return render(request, 'trainee/list.html', {'trainees': trainees})
def addTrainee(request):
    return render(request, 'trainee/add_trainee.html')
def updateTrainee(request, id):
    return HttpResponse(f'<h1>Update trainee number:{id}</h1>')
def deleteTrainee(request, id):
    return HttpResponse(f'<h1>Delete trainee number:{id}</h1>')