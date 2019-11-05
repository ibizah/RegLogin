from django.shortcuts import render, get_object_or_404
from .forms import EmpForm, UserForm, UserProfileForm, RegForm
from .models import Employee
#from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.decorators import api_view

#from rest_framework import status
from .serializers import EmployeeSerializers
from django.contrib.auth.forms import UserCreationForm
# imports for login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from demoapp import views


class Empview(APIView):
    def get(self,request):
        employee= Employee.objects.all()
        serializer= EmployeeSerializers(employee, many=True)
        return Response(serializer.data)

    def post(self,slug):
        pass


@api_view(['PUT', ])
def Empupdate(request,slug):

    employee=Employee.objects.get(slug=slug)

    if request.method=='PUT':
        serializer= EmployeeSerializers(employee, data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['success']=' update Successful'
            return Response(data=data)
        return Response(serializer.errors)

@api_view(['DELETE', ])
def Empdelete(request, slug):

    employee=Employee.objects.get(slug=slug)

    if request.method=='DELETE':
        operation= employee.delete()
        data={}
        if operation:
            data['success']='delete succesful'
        else:
            data['failure']='delete failed'

@api_view(['POST', ])
def EmpCreate(request):
    employee=Employee.objects.create(fname=request.data['fname'],email=request.data['email'], age=request.data['age'])
    serializer=Employee(employee,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error)
# Create your views here.

def home(request):
    if request.method == 'POST':
        username= request.POST.get('username', 'not available')

    form=EmpForm(request.POST or None)
    #data= Employee.objects.all()
    d={}

    if request.method=='POST' and form.is_valid():
        form=EmpForm(request.POST )

        fn=form.cleaned_data['fname']
        em=form.changed_data['email']
        age=form.cleaned_data['age']
        #
        d={'fn':fn, 'em':em, 'age':age}
        print(f'my name is {d["fn"]} ')
        #
        d={'data':data, 'username':username}

    return render(request, 'home.html', d)

def form(request):
    form=EmpForm()
    if request.method =='POST' and form.is_valid():
        form=EmpForm(request.POST)
        form.save(commit=True)
    d={'form':form}

    return render(request, 'form.html', d )

#***********************************************************************



def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user= user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered= True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form= UserForm()
        profile_form= UserProfileForm()

    return render(request,'registration.html', {'registered':registered, 'user_form':user_form, 'profile_form':profile_form} )


#***************************************************************************


def reg(request):
    register = False
    userform =RegForm()
    d={}

    if request.method =='POST':
        userform = RegForm(data=request.POST)
        if userform.is_valid():
            # name= userform.cleaned_data['username']
            # email= userform.cleaned_data['email']
            # print('*******************************')
            # print(f'your name is {name} email is {email}')

            form=userform.save()
            form.set_password(form.password)
            form.save()
            register= True

            d={'username':name, 'email':email}




        else:
            print(userform.errors)
    else:
        form= RegForm()


    return render(request, 'reg.html',d,{'form':userform, 'register':register})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('demoapp:home'))


@login_required
def special(request):
    return HttpResponse('you are logged in , nice')


def  user_login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user=  authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('demoapp:home'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('someone tried to login and failed')
            print(f'username: {username} and password: {password}')
            return HttpResponse(f'invalid login details supplied for {username}')

    else:
        return render(request, 'login.html')
