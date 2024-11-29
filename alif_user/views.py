from django.shortcuts import render,redirect
from alif_admin.models import Participant
from datetime import datetime
from django.utils.timezone import localtime,now
from .decorator import auth_user

@auth_user
def dashboard(request):
    return render(request,'user/dashboard.html')

@auth_user
def participants_list(request):
    
    if request.method == 'POST':
        category = request.POST['category']
        participants = Participant.objects.filter(category = category)
        if 'student_id' in request.POST:
            print(request.POST['student_id'])
            selected_participant = Participant.objects.get(id = request.POST['student_id'])
            selected_participant.report_status = 'reported'

            current_time = localtime(now()).strftime('%I:%M %p')
            print(current_time) 
            selected_participant.report_time = current_time
            selected_participant.save()
        return render(request,'user/ParticipantsList.html', {'participants':participants,'category':category})
    return render(request,'user/ParticipantsList.html')


def logout(request):
    del request.session['user_id']
    del request.session['user_name']
    request.session.flush()
    return redirect('common:admin_login')
