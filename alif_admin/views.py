from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,JsonResponse
import random

from django.db.models.functions import Round
from django.db.models import Sum
from . import utils

from django.views.decorators.csrf import csrf_exempt
from .decorator import auth_admin


@auth_admin
def dashboard(request):
    return render(request,'alif_admin/dashboard.html')


@auth_admin
def register_student(request):
    message = ''
    if request.method == 'POST':
        participant_name = request.POST['participant_name'].lower()
        admission_no = request.POST['admission_no']
        student_cls = request.POST['student_cls']
        division = request.POST['division']
        category = request.POST['category']



        record = Participant.objects.filter(admission_no = admission_no)

        if not record:
            _ = Participant(
                        student_name = participant_name, 
                        admission_no=admission_no,
                         student_cls=student_cls,
                         division=division,
                         category = category
                         ).save()
            message = 'Student Added Succesfully '

        else:
            message = 'Admission No Exist'

    return render(request,'alif_admin/registerStudent.html', {'message': message})


@auth_admin
def generate_code_letter(request):
    if request.method == 'POST':
        category = request.POST['category']
        participants = Participant.objects.filter(category = category)
        return render(request,'alif_admin/generateCodeLetter.html', {'participants':participants,'category':category})

    return render(request,'alif_admin/generateCodeLetter.html')

@csrf_exempt
def get_code(request):
    participant = Participant.objects.get(id = request.POST['participantId'])

    if participant.code_letter == "":
        code = utils.getCode(request.POST['category'])
        print(code)
        participant.code_letter = code
        participant.save()

    else:
        code = 'Code Letter Already Generated'

    return JsonResponse({'letter': code})
@auth_admin
def results(request):
    if request.method == 'POST':

        
        category = request.POST['category']
        # participants = Score.objects.filter(student__category = category).annotate(total_marks=Sum('total')).order_by('student__category', 'student__student_name')
        student_scores = (
        Score.objects.filter(student__category=category)  # Filter by category
        .values('student__id', 'student__student_name',
                'student__admission_no', 'student__category',
                 'student__student_cls',
                  'student__division',
                   'student__code_letter'
                )
        .annotate(total_marks=Round(Sum('total'),2))
        .order_by('-total_marks')
    )
        if 'download' in request.POST:
            print('downloading........')
            file_name = category + '-results'
            pdf = utils.render_to_pdf('alif_admin/result_download.html', {'participants':student_scores,'category':category})
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=' + file_name +'.pdf'
            return response

        return render(request,'alif_admin/results.html',{'participants':student_scores,'category':category})
    return render(request,'alif_admin/results.html')


def logout(request):
    del request.session['admin_id']
    request.session.flush()
    return redirect('common:admin_login')
@auth_admin
def view_details(request,id):
    
    record = Score.objects.filter(student__id  = id).order_by('judge')
    student = record[0].student.student_name
    admission_no = record[0].student.admission_no

    return render(request,'alif_admin/viewDetails.html', {'record':record, 'student': student,'admission_no':admission_no})

    # return render(request,'alif_admin/generateCodeLetter.html')
