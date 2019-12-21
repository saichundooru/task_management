from django.shortcuts import render
from admin_app.models import EmployeeModel,TaskAssigning
from django import  forms
from django.contrib import messages
from django.shortcuts import redirect,render

def user_login(request):
    uID=request.POST.get('userid')
    pwd=request.POST.get('password')
    try:
        check = EmployeeModel.objects.get(contactNo=uID,password=pwd)
        print(check)
        request.session['empID'] = check.empID
        return render(request,'user/user_taskbar.html',{'welcome_user': True,'data1':check})
    except:
        return render(request, 'user/user_login_page.html',{'message': 'Invalid User Details'})


def user_logout(request):
    return render(request,'user/user_login_page.html')


def change_pwd(request):
    return render(request,'user/user_taskbar.html',{'change_pwd': True})


def save_pwd(request):
    emailid= request.POST.get('email_id')
    oldpwd =request.POST.get('old_pwd')
    newpwd=request.POST.get('new_pwd')
    confirmpwd=request.POST.get('confirm_pwd')
    if newpwd==confirmpwd:
      res=EmployeeModel.objects.get(emailID=emailid,password=oldpwd)
      res.password=newpwd
      res.save()
      return render(request,'user/user_taskbar.html',{'change_pwd': True,'message':'Password changes successully'})
    else:
        return render(request,'user/user_taskbar.html',{'change_pwd': True,'message':'Enter correct details to change'})


def view_task(request):
    # session_id = request.session['empID']
    # print(session_id)
    # try:
    #     res1 = TaskAssigning.objects.filter(empID_id=session_id,status='pending')
    #     print(res1)
    #     # print(res1.taskname)
    #     # print(res1.taskno)
    #     # print(res1.empID.status)
    #     # if res1.empID.status == 'pending':
    #     return render(request,'user/view_task.html',{'data':res1})
    #     # else:
    #     #     return render(request,'user/view_task.html',{"message": "Task Completed Till Now not Assinged"})
    # except:
    #     return render(request, 'user/view_task.html', {"msg": "Task Till Now not Assinged"})
    res=request.session['empID']
    i = TaskAssigning.objects.filter(status='pending',empID_id=res)
    return render(request, 'user/view_task.html',{"data": i,"msg":"Task Completed Till Now not Assinged"})

def task_completed(request):
    na = request.GET['name']
    print(na)
    i = TaskAssigning.objects.get(taskname=na)
    i.status = 'completed'
    i.save()
    return redirect('viewtask')