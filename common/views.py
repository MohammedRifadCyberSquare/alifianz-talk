from django.shortcuts import render,redirect
from alif_admin.models import AlifAdmin
from judges.models import *


def admin_login(request):
    message = ''
    if request.method == 'POST':
        admin_id = request.POST['admin_id']
        password = request.POST['password']

        record = AlifAdmin.objects.filter(admin_id = admin_id, password = password)
        print(record)
        if record:
            request.session['admin_id'] = record[0].id
             
            return redirect('alif_admin:dashboard')

        else:
            print('here')
            message = 'User Name or Password Incorrect'
    return render(request,'common/adminLogin.html', {'message': message})


def judges_login(request):
    message = ''
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']

        record = Judge.objects.filter(user_name = user_name, password = password)
        print(record)
        if record:
            request.session['judge_id'] = record[0].id
            request.session['judge_name'] = record[0].judge_name
             
            return redirect('judges:dashboard')

        else:
            print('here')
            message = 'User Name or Password Incorrect'
    return render(request,'common/judgesLogin.html', {'message': message})
