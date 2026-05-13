from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from course.models import Course
from trainee.forms import *
from .models import *


# Create your views here.

# def traineeList(request):
#     return render(request, 'trainee/list.html', {'trainees': Trainee.objects.all()})

##& trainee list -> generic view ##
class TraineeListGeneric(LoginRequiredMixin, ListView):
    model = Trainee
    template_name = 'trainee/list.html'
    context_object_name = 'trainees'

@login_required
def traineeDetails(request, id):
    trainee = Trainee.objects.get(id=id)
    return render(request, 'trainee/details.html', {'trainee': trainee})

##? Add trainee -> function based view ##
# def addTrainee(request):
#     if request.method == 'POST':
#         ###^ using ModelForm ### 
#         form = TraineeFormModel(data = request.POST, files = request.FILES)
#         if form.is_valid():
#             form.save() 
#             return redirect('TraineeList')
        

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
        
    # else:
    #     form = TraineeFormModel()
    # return render(request, 'trainee/add_trainee.html', {'form': form})

##? Add trainee -> class based view ##
# class AddTraineeView(View):
#     def get(self, request):
#         return render(request, 'trainee/add_trainee.html', {'form': TraineeFormModel()})
    
#     def post(self, request):
#         form = TraineeFormModel(data = request.POST, files = request.FILES)
#         if form.is_valid():
#             form.save() 
#             return redirect('TraineeList')
#         return render(request, 'trainee/add_trainee.html', {'form': form})
    
##* Add trainee -> generic view ##
class AddTraineeGeneric(LoginRequiredMixin, CreateView):
    model = Trainee
    template_name = 'trainee/add_trainee.html'
    form_class = TraineeFormModel
    success_url = reverse_lazy('TraineeList')


@login_required
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

@login_required
def deleteTrainee(request, id):
    trainee = Trainee.objects.get(id=id)
    
    if request.method == 'POST':
        trainee.delete()
        return redirect('TraineeList')

    return render(request, 'trainee/delete.html', {'trainee': trainee})