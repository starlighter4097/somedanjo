from django.shortcuts import render,redirect
from .models import attendance
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']

        if username == "teacher":
            return redirect('/attendancesheet')
        if username == "tutor":
            return redirect('/view')

        else:
            return redirect('/home')

    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html') 



def Modify(request):
    return render(request, 'Modify.html') 




def attendancesheet(request):
    if request.method=='POST':
        std_no=request.POST.get('')
        std_name=request.POST.get('')
        period1=request.POST.get('chk')
        period2=request.POST.get('chk1')
        period3=request.POST.get('chk2')
        period4=request.POST.get('chk3')
        period5=request.POST.get('chk4')
        period6=request.POST.get('chk5')
        period7=request.POST.get('chk6')
        std_obj = attendance()
        std_obj.Roll_no=std_no
        std_obj.Student_Name=std_name
        std_obj.Period1=period1
        std_obj.Period2=period2
        std_obj.Period3=period3
        std_obj.Period4=period4
        std_obj.Period5=period5
        std_obj.Period6=period6
        std_obj.Period7=period7
        std_obj.save()
        return viewattendancesheet(request)

    
    return render(request, 'attendancesheet.html')




def Add(request):
    return render(request, 'Add.html', {'formset': formset})
