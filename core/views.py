from django.shortcuts import render, redirect

from rest_framework import status
from rest_framework.response import Response

from .form import RegisterForm
from .models import Register,Login
# Create your views here.
from rest_framework import viewsets 

from .serializers import RegisterSerializer,LoginSerializer




class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer





def home_view(request):
    return render(request, 'core/index.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            age = form.cleaned_data['age']
            firstname = form.cleaned_data['FirstName']
            surname = form.cleaned_data['SurName']
            hiv_status = form.cleaned_data['Hiv_status']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            register = Register(
                username=username,
                age=age,
                FirstName=firstname,
                SurName=surname,
                Hiv_status=hiv_status,
                phone_number=phone_number,
                email=email,
                password=password
            )
            register.save()
            print(form.cleaned_data)
    else:
        form = RegisterForm()

    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            login = Login(
                username=username,
                password=password
            )
            login.save()
            # go to home page
            return redirect('register')
    else:
        form = RegisterForm()
    return render(request, 'core/login.html')



    