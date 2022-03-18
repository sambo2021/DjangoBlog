
from django.shortcuts import render , HttpResponse ,redirect
from .models import Student, Track
from .forms import StudentForm , TrackForm
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response 

# Create your views here.

def home(request):
    students = Student.objects.all()
    context = {'all_students': students}
    return render(request , 'myapp/home.html',context)

def show(request,st_id):
    st = Student.objects.get(id=st_id)
    context = { 'st': st}
    return render(request , 'myapp/show.html',context)

def stDel(request , st_id):
     st = Student.objects.get(id=st_id)
     st.delete()
     return redirect('home')

def stAdd(request):
    form = StudentForm()
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'myapp/form.html' , context)

def stEdit(request, st_id):
    st=Student.objects.get(id=st_id)
    form  =StudentForm(instance = st)
    if request.method=='POST':
        form  =StudentForm(request.POST,instance = st)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request , 'myapp/form.html', context)



#Rest API views 


@api_view(['GET','POST','DELETE'])
def api_students_all(request):
    students = Student.objects.all()
    st_ser = StudentSerializer(students,many =True)
    return Response(st_ser.data)

@api_view(['GET'])
def api_students_show(request,st_id):
    st = Student.objects.get(id = st_id)
    st_ser = StudentSerializer(st , many=False)
    return Response(st_ser.data)


@api_view(['POST'])
def api_students_add(request):
    st_ser = StudentSerializer(data = request.data)
    if st_ser.is_valid():
        st_ser.save()
        return redirect ('api-add')

@api_view(['POST'])
def api_students_edit(request, st_id):
    st = Student.objects.get(id = st_id)
    st_ser = StudentSerializer(data = request.data, instance=st)
    if st_ser.is_valid():
        st_ser.save()
        return redirect ('api-all')

@api_view(['DELETE'])
def api_students_del(request, st_id):
    st = Student.objects.get(id = st_id)
    st.delete()
    return Response ('student has been deleted')
 

