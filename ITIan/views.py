from django.shortcuts import redirect, render


def register(request):
    return render(request, 'registration/register.html')
def login(request):
    return render(request, 'registration/login.html')
def logout(request):
    return redirect('Login')   

