from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Student, Track
from .forms import StudentForm, UserForm
#rest_framework imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
#auth imports.
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

#auth views.
def loginPg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(username= name, password =passwd)
            if user is not None:
                login(request, user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')
                
            else:
                messages.info(request, 'User name or password is incorrect')
        return render(request, 'tunapp/login.html')

def signoutPg(request):
    logout(request)
    return redirect('login')

def signupPg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        signup_form = UserForm()
        if(request.method =='POST'):
            signup_form = UserForm(request.POST)
            if(signup_form.is_valid()):
                signup_form.save()
                msg = 'User account created for username: ' + signup_form.cleaned_data.get('username')
                messages.info(request, msg)
                return redirect('login')
        context = {'signup_form': signup_form}
        return render(request, 'tunapp/signup.html', context)

#rest_framework views.
@api_view(['GET'])
def api_all_students(request):
    all_st = Student.objects.all()
    sr_serializer = StudentSerializer(all_st, many=True)
    return Response(sr_serializer.data)

@api_view(['GET'])
def api_student_details(request,st_id):
    all_st = Student.objects.get(id=st_id)
    sr_serializer = StudentSerializer(all_st, many=False)
    return Response(sr_serializer.data)

@api_view(['POST'])
def api_student_create(request):
    sr_serializer = StudentSerializer(data=request.data)
    if sr_serializer.is_valid():
        sr_serializer.save()
    return redirect('api-list')

@api_view(['POST'])
def api_student_edit(request, st_id):
    st = Student.objects.get(id = st_id)
    sr_serializer = StudentSerializer(instance = st, data=request.data)
    if sr_serializer.is_valid():
        sr_serializer.save()
    return redirect('api-list')

@api_view(['DELETE'])
def api_student_delete(request, st_id):
    st = Student.objects.get(id = st_id)
    st.delete()
    return Response('User Deleted')


# Create your views here.
def ListAllStudents(request):
    return HttpResponse('<h1>This is List all student response </h1>')

def ListStudentDetails(request, st_id):
    st = Student.objects.get(id = st_id)
    context = {'st': st}
    return render(request,'tunapp/st-details.html', context)

@login_required(login_url='login')
def home(request):
    all_student =  Student.objects.all()
    conxt = {'students': all_student}
    return render(request,'tunapp/home.html', conxt)
def studentDel(request, st_id):
    st = Student.objects.get(id=st_id)
    st.delete()
    return redirect('home')
@login_required(login_url='login')
def addStudent(request):
    if request.method == 'POST':
        st_form = StudentForm(request.POST)
        if st_form.is_valid():
            st_form.save()
            return redirect('home')
    st_form = StudentForm()
    context = {'form': st_form}
    return render(request, 'tunapp/add-student.html', context)

def editStudent(request, st_id):
    student = Student.objects.get(id=st_id)
    st_form = StudentForm(instance=student)

    if request.method =='POST':
        st_form = StudentForm(request.POST, instance=student)
        if st_form.is_valid():
            st_form.save()
            return redirect('home')
    context={'form': st_form}
    return render(request, 'tunapp/add-student.html', context)
