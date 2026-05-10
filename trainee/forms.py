from django import forms
from course.models import Course
from trainee.models import Trainee


class TraineeForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter trainee name'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Enter trainee email'
    }))
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'placeholder': 'Enter phone number'
    }))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'Enter trainee age'
    }))
    course = forms.ChoiceField(
        choices=[(course.id, course.name) for course in Course.objects.all()],
        widget=forms.Select(attrs={
            'style': 'padding: 10px; border: #bfc5cb solid 1px; border-radius: 4px;'
    }))

class TraineeFormModel(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = '__all__'