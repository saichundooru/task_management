from django.shortcuts import render, redirect
from admin_app.forms import Taskform
from admin_app.models import EmployeeModel, TaskAssigning


def home_page(request):
    return render(request, 'home_page.html')


def admin_page(request):
    return render(request, 'admin/admin_loginpage.html')


def admin_login(request):
    userid1 = request.POST.get('userid')
    password1 = request.POST.get('password')
    if userid1 == 'admin' and password1 == 'admin':
        return render(request, 'admin/admin_access.html')
    else:
        return render(request, 'admin/admin_loginpage.html', {'message': " Invalid User details"})


def user_page(request):
    return render(request, 'user/user_login_page.html')

def admin_logout(request):
    return redirect('admin_page')

def create_user(request):
    return render(request,'admin/admin_taskbar.html',{'create_user':True})


def saving_userdetails(request):
    id = request.POST.get('empid')
    name = request.POST.get('empname')
    cno = request.POST.get('cno')
    email = request.POST.get('email')
    des = request.POST.get('designation')
    pwd = request.POST.get('pwd')
    EmployeeModel(empID=id, empName=name, contactNo=cno, emailID=email, designation=des, password=pwd).save()
    return render(request, 'admin/admin_taskbar.html',{'create_user': True, 'message': 'Details Saved Sucessfully'})


def view_users(request):
    data=EmployeeModel.objects.all()
    return render(request,'admin/admin_taskbar.html',{'view_users':data})


def assign_task(request):
    return render(request,'admin/admin_taskbar.html',{'assign_task':True,'form': Taskform()})

def view_task(request):
    db1 = TaskAssigning.objects.all()
    #db2 = TaskAssigning.objects.values_list('taskname')
    return render(request, 'admin/admin_taskbar.html', {'task_data1': True, 'x1': db1})


def save_task(request):
    taskname=request.POST['taskname']
    empId=request.POST['empID']
    TaskAssigning(taskname=taskname,empID_id=empId,status='pending').save()
    return redirect('assign_task')


def delete(request):
    tno = request.GET['tno']
    TaskAssigning.objects.get(taskno=tno).delete()
    return redirect('view_task')